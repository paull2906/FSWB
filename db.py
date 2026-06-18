import hashlib
from pathlib import Path
import json
import click
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class User(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    city = db.Column(db.String(120), nullable=True)

    quizzes = db.relationship('Quiz', back_populates='creator', cascade='all, delete-orphan')
    scores = db.relationship('Score', back_populates='user', cascade='all, delete-orphan')

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    main_genre_id = db.Column(db.Integer, db.ForeignKey('main_genre.id'), nullable=True)
    subgenre_id = db.Column(db.Integer, db.ForeignKey('subgenre.id'), nullable=True)
    difficulty = db.Column(db.String(120), nullable=True)

    creator = db.relationship('User', back_populates='quizzes')
    main_genre = db.relationship('MainGenre', back_populates='quizzes')
    subgenre = db.relationship('Subgenre', back_populates='quizzes')
    scores = db.relationship('Score', back_populates='quiz', cascade='all, delete-orphan')
    songs = db.relationship('Song', back_populates='quiz', cascade='all, delete-orphan', order_by="Song.position")

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    itunes_id = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album = db.Column(db.String, nullable=False)
    preview_url = db.Column(db.String)
    cover_url = db.Column(db.String)
    position = db.Column(db.Integer, nullable=False)

    quiz = db.relationship('Quiz', back_populates='songs')

class MainGenre(db.Model):
    """Oberkategorie, z.B. 'Metal', 'Electronic', 'Jazz'."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
 
    subgenres = db.relationship('Subgenre', back_populates='main_genre', cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', back_populates='main_genre')
 
    def __repr__(self):
        return f'<MainGenre {self.name}>'
 
class Subgenre(db.Model):
    """Nischen-Subgenre, z.B. 'Djent', 'Blackened Sludge', 'Vaportrap'."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    main_genre_id = db.Column(db.Integer, db.ForeignKey('main_genre.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'main_genre_id', name='uq_subgenre_name_main'),
    )
 
    main_genre = db.relationship('MainGenre', back_populates='subgenres')
    quizzes = db.relationship('Quiz', back_populates='subgenre')
 
    def __repr__(self):
        return f'<Subgenre {self.name} ({self.main_genre.name})>'
    
def import_genres_from_json(path):
    genre_map = parse_genres_json(path)
    existing_main = {
        mg.name.casefold(): mg
        for mg in MainGenre.query.all()
    }

    added_main = 0
    added_sub = 0
    skipped = 0

    for main_name, sub_names in genre_map.items():
        key = main_name.casefold()

        if key not in existing_main:
            main_genre = MainGenre(name=main_name)
            db.session.add(main_genre)
            db.session.flush()
            existing_main[key] = main_genre
            added_main += 1
        else:
            main_genre = existing_main[key]

        existing_subs = {
            sg.name.casefold()
            for sg in Subgenre.query.filter_by(main_genre_id=main_genre.id).all()
        }

        for sub_name in sub_names:
            sub_key = sub_name.casefold()
            if sub_key not in existing_subs:
                db.session.add(Subgenre(name=sub_name, main_genre_id=main_genre.id))
                existing_subs.add(sub_key)
                added_sub += 1
            else:
                skipped += 1

    db.session.commit()
    return added_main, added_sub, skipped

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', back_populates='scores')
    quiz = db.relationship('Quiz', back_populates='scores')


def parse_genres_json(path):
    """
    Liest genres.json und gibt ein Dict { hauptgenre_name: [subgenre_name, ...] } zurück.
    """
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
 
    # Sicherstellen, dass alle Werte Listen sind
    parsed = {}
    for main_name, subs in data.items():
        main_name = main_name.strip()
        if not main_name:
            continue
        parsed[main_name] = [s.strip() for s in subs if s.strip()]
 
    return parsed
 
 


def insert_sample_data():
    admin = User(username='admin', password_hash=hash_password('1234'), is_admin=True)
    user1 = User(username='BerlinPlayer', password_hash=hash_password('1234'), city='Berlin')
    user2 = User(username='ViennaPlayer', password_hash=hash_password('1234'), city='Vienna')
    main_electronic = MainGenre(name='Electronic')
    main_jazz = MainGenre(name='Jazz')
    db.session.add_all([admin, user1, user2, main_electronic, main_jazz])
    db.session.commit()

    sub_techno = Subgenre(name='Techno', main_genre_id=main_electronic.id)
    sub_house = Subgenre(name='House', main_genre_id=main_electronic.id)
    sub_bebop = Subgenre(name='Bebop', main_genre_id=main_jazz.id)
    sub_fusion = Subgenre(name='Jazz Fusion', main_genre_id=main_jazz.id)
    db.session.add_all([sub_techno, sub_house, sub_bebop, sub_fusion])
    db.session.commit()

    quiz1 = Quiz(title='Electronic Starter', creator_id=admin.id, main_genre_id=main_electronic.id, subgenre_id=sub_techno.id, difficulty='Easy')
    quiz2 = Quiz(title='Jazz Classics', creator_id=user1.id, main_genre_id=main_jazz.id, subgenre_id=sub_bebop.id, difficulty='Medium')
    db.session.add_all([quiz1, quiz2])
    db.session.commit()

    songs = [
        Song(quiz_id=quiz1.id, itunes_id='0', title='Strobe', artist='Deadmau5',
            album='For Lack of a Better Name', preview_url='', cover_url='', position=1),
        Song(quiz_id=quiz1.id, itunes_id='0', title='Stayin Alive', artist='Boys Noize',
          album='Oi Oi Oi', preview_url='', cover_url='', position=2),
        Song(quiz_id=quiz2.id, itunes_id='0', title='Take Five', artist='Dave Brubeck',
         album='Time Out', preview_url='', cover_url='', position=1),
        Song(quiz_id=quiz2.id, itunes_id='0', title='Fly Me to the Moon', artist='Frank Sinatra',
            album='It Might as Well Be Swing', preview_url='', cover_url='', position=2),
     ]
    db.session.add_all(songs)
    db.session.commit()

    scores= [
        Score(user_id=user1.id, quiz_id=quiz1.id, points=150),
        Score(user_id=user2.id, quiz_id=quiz1.id, points=200),
    ]
    db.session.add_all(scores)
    db.session.commit()


def init_db(app):
    Path(app.config['DATABASE']).parent.mkdir(parents=True, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE']
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @click.command('init-db')
    def init_db_command():
        with app.app_context():
            db.drop_all()
            db.create_all()
            insert_sample_data()
            click.echo('Datenbank initialisiert')

    @click.command('import-genres')
    @click.argument('path', type=click.Path(exists=True, dir_okay=False, path_type=Path))
    def import_genres_command(path):
        """Haupt- und Subgenres aus einer genres.json importieren."""
        with app.app_context():
            db.create_all()
            added_main, added_sub, skipped = import_genres_from_json(path)
        click.echo(
            f'Import abgeschlossen: '
            f'{added_main} neue Hauptgenres, '
            f'{added_sub} neue Subgenres, '
            f'{skipped} bereits vorhanden.'
        )
 
    app.cli.add_command(init_db_command)
    app.cli.add_command(import_genres_command)

