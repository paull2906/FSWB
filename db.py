import hashlib
import json
import click
from flask_sqlalchemy import SQLAlchemy
from app import app
from itunes import search_tracks, format_track

# Pfad zur SQLite-Datenbank (drei Slashes = sqlite:// + relativer Pfad)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musikquiz.sqlite'

# ORM-Objekt zunächst ohne App erzeugen und erst danach binden
# (deferred init -> vermeidet zirkulaere Importe)
db = SQLAlchemy()
db.init_app(app)


def hash_password(password):
    #Bildet den SHA-256-Hash eines Passworts als 64-stelligen Hex-String.
    return hashlib.sha256(password.encode()).hexdigest()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)  # 64 Zeichen = SHA-256-Hex
    is_admin = db.Column(db.Boolean, default=False)
    city = db.Column(db.String(120), nullable=True)

    # Beziehungen: löscht man einen User, werden Quizze und Scores mitgeloescht
    quizzes = db.relationship('Quiz', back_populates='creator', cascade='all, delete-orphan')
    scores = db.relationship('Score', back_populates='user', cascade='all, delete-orphan')

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    # Fremdschluessel verweisen auf Tabellennamen
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    main_genre_id = db.Column(db.Integer, db.ForeignKey('main_genre.id'), nullable=True)
    subgenre_id = db.Column(db.Integer, db.ForeignKey('subgenre.id'), nullable=True)
    difficulty = db.Column(db.String(120), nullable=True)

    creator = db.relationship('User', back_populates='quizzes')
    main_genre = db.relationship('MainGenre', back_populates='quizzes')
    subgenre = db.relationship('Subgenre', back_populates='quizzes')
    scores = db.relationship('Score', back_populates='quiz', cascade='all, delete-orphan')
    # Songs werden automatisch nach ihrer Position sortiert geladen
    songs = db.relationship('Song', back_populates='quiz', cascade='all, delete-orphan',
        order_by="Song.position")


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    itunes_id = db.Column(db.String, nullable=False)   # ID aus der iTunes-Search-API
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album = db.Column(db.String, nullable=False)
    preview_url = db.Column(db.String)  # nicht jeder Treffer hat eine Vorschau
    cover_url = db.Column(db.String)
    position = db.Column(db.Integer, nullable=False)   # Reihenfolge im Quiz

    quiz = db.relationship('Quiz', back_populates='songs')

class MainGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    # Subgenres hängen am Hauptgenre. Quizze werden bewusst nicht mitgelöscht
    subgenres = db.relationship('Subgenre', back_populates='main_genre', cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', back_populates='main_genre')

class Subgenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)  # nur je Hauptgenre eindeutig, nicht global
    main_genre_id = db.Column(db.Integer, db.ForeignKey('main_genre.id'), nullable=False)

    # Name + Hauptgenre muessen zusammen eindeutig sein
    # -> gleicher Subgenre-Name darf unter verschiedenen Hauptgenres existieren
    __table_args__ = (
        db.UniqueConstraint('name', 'main_genre_id', name='uq_subgenre_name_main'),
    )

    main_genre = db.relationship('MainGenre', back_populates='subgenres')
    quizzes = db.relationship('Quiz', back_populates='subgenre')

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', back_populates='scores')
    quiz = db.relationship('Quiz', back_populates='scores')


# Legt alle Tabellen an, falls sie noch nicht existieren (ändert bestehende nicht)
with app.app_context():
    db.create_all()


@click.command('init-db')
def init():
    #CLI-Befehl `flask init-db`: DB komplett zurücksetzen und mit Beispieldaten fuellen.
    with app.app_context():
        db.drop_all()      # löscht alle bestehenden Daten
        db.create_all()
        insert_sample()
    click.echo('Database has been initialized.')


app.cli.add_command(init)


@click.command('import-genres')
@click.argument('path')
def import_genres(path):
    #CLI-Befehl `flask import-genres <path>`: Genres aus einer JSON-Datei importieren.
    with app.app_context():
        db.create_all()
        added_main, added_sub = import_genres_from_json(path)
    click.echo(f'Import done: {added_main} main genres, {added_sub} subgenres.')


app.cli.add_command(import_genres)


def import_genres_from_json(path):
    """Importiert Haupt- und Subgenres aus einer JSON-Datei.

    Erwartetes Format: {"Electronic": ["Techno", "House"], ...}
    Idempotent: bereits vorhandene Genres werden uebersprungen, keine Duplikate.
    Gibt die Anzahl neu angelegter (Hauptgenres, Subgenres) zurueck.
    """
    with open(path, encoding='utf-8') as f:   # UTF-8 wichtig für Umlaute in Genrenamen
        genre_map = json.load(f)

    added_main = 0
    added_sub = 0

    for main_name, sub_names in genre_map.items():
        # Prüfen, ob das Hauptgenre schon existiert (SQLAlchemy-2.x-Syntax)
        main_genre = db.session.execute(
            db.select(MainGenre).filter_by(name=main_name)
        ).scalar()
        if main_genre is None:
            main_genre = MainGenre(name=main_name)
            db.session.add(main_genre)
            db.session.flush()   # schreibt in die Transaktion -> main_genre.id ist sofort verfügbar
            added_main += 1

        for sub_name in sub_names:
            # Eindeutigkeit über Name + Hauptgenre pruefen (passend zum UniqueConstraint)
            exists = db.session.execute(
                db.select(Subgenre).filter_by(name=sub_name, main_genre_id=main_genre.id)
            ).scalar()
            if exists is None:
                db.session.add(Subgenre(name=sub_name, main_genre_id=main_genre.id))
                added_sub += 1

    db.session.commit()   # ein einziger Commit fuer den gesamten Import
    return added_main, added_sub


def fetch_song(query, quiz_id, position):
    """Sucht einen Track ueber die iTunes-API und baut daraus ein Song-Objekt.

    `query` ist ein Suchbegriff (z.B. 'Deadmau5 Strobe'), kein URL.
    Gibt None zurueck, wenn kein Treffer gefunden wird.
    Der Song wird NICHT gespeichert, nur erzeugt und zurueckgegeben.
    """
    results = search_tracks(query, limit=1)   # nur den besten Treffer holen
    if not results:
        return None
    t= format_track(results[0])   # rohen API-Treffer in sauberes Dict umwandeln
    return Song(
        quiz_id=quiz_id,
        itunes_id=t['itunes_id'],
        title=t['title'],
        artist=t['artist'],
        album=t['album'],
        preview_url=t['preview_url'],
        cover_url=t['cover_url'],
        position=position
    )


def insert_sample():
    """Fuellt die Datenbank mit Beispieldaten (Users, Genres, Quizze, Songs, Scores)."""
    # Bestehende Daten löschen; Reihenfolge von abhängig -> Eltern,
    # damit keine Fremdschlüssel-Constraints verletzt werden
    for model in [Score, Song, Quiz, Subgenre, MainGenre, User]:
        db.session.execute(db.delete(model))

    # Beispiel-User (Passwörter werden gehasht)
    admin = User(username='admin', password_hash=hash_password('1234'), is_admin=True)
    user1 = User(username='BerlinPlayer', password_hash=hash_password('1234'), city='Berlin')
    user2 = User(username='ViennaPlayer', password_hash=hash_password('1234'), city='Vienna')

    # Beispiel-Hauptgenres
    electronic = MainGenre(name='Electronic')
    jazz = MainGenre(name='Jazz')
    rap = MainGenre(name='Hip-Hop / Rap')
    db.session.add_all([admin, user1, user2, electronic, jazz, rap])
    db.session.commit()   # Commit nötig, damit die Objekte danach IDs haben

    # Subgenres verweisen auf die gerade erzeugten Hauptgenre-IDs
    techno = Subgenre(name='Techno', main_genre_id=electronic.id)
    bebop = Subgenre(name='Bebop', main_genre_id=jazz.id)
    gangsta_rap = Subgenre(name='West Coast Hip-Hop', main_genre_id=rap.id)
    db.session.add_all([techno, bebop, gangsta_rap])
    db.session.commit()

    # Beispiel-Quizze, jeweils mit Ersteller, Haupt- und Subgenre verknüpft
    quiz1 = Quiz(title='Electronic Starter', creator_id=admin.id, main_genre_id=electronic.id, subgenre_id=techno.id, difficulty='Easy')
    quiz2 = Quiz(title='Jazz Classics', creator_id=user1.id, main_genre_id=jazz.id, subgenre_id=bebop.id, difficulty='Medium')
    quiz3 = Quiz(title='90s West Coast Hip Hop', creator_id=user2.id, main_genre_id=rap.id, subgenre_id=gangsta_rap.id, difficulty='Hard')
    db.session.add_all([quiz1, quiz2, quiz3])
    db.session.commit()

    # Songs über die iTunes-API holen: (Suchbegriff, quiz_id, position)
    song_urls = [
         ('Deadmau5 Strobe',            quiz1.id, 1),
        ('Boys Noize Oi Oi Oi',        quiz1.id, 2),
        ('Dave Brubeck Take Five',     quiz2.id, 1),
        ('Frank Sinatra Fly Me to the Moon', quiz2.id, 2),
        ('N.W.A. Straight Outta Compton', quiz3.id, 1),
        ('Ice Cube You Know How We Do It', quiz3.id, 2),
        ('2Pac All About U', quiz3.id, 3),
        ('Westside Connection Bow Down', quiz3.id, 4),
    ]

    # Nur tatsaechlich gefundene Songs übernehmen (macht echte Netzwerk-Requests)
    songs = []
    for url, quiz_id, position in song_urls:
            song= fetch_song(url, quiz_id, position)
            if song:
                songs.append(song)

    # Beispiel-Scores
    scores = [
        Score(user_id=user1.id, quiz_id=quiz1.id, points=150),
        Score(user_id=user2.id, quiz_id=quiz1.id, points=200),
        Score(user_id=user1.id, quiz_id=quiz2.id, points=100),
        Score(user_id=user2.id, quiz_id=quiz3.id, points=200),
    ]

    db.session.add_all(songs + scores)   # Songs und Scores zusammen in einem Commit speichern
    db.session.commit()