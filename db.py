import hashlib
import json
import click
from flask_sqlalchemy import SQLAlchemy
from app import app
from itunes import search_tracks, format_track

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musikquiz.sqlite'

db=SQLAlchemy()
db.init_app(app)


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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
 
    subgenres = db.relationship('Subgenre', back_populates='main_genre', cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', back_populates='main_genre')
 
 
class Subgenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    main_genre_id = db.Column(db.Integer, db.ForeignKey('main_genre.id'), nullable=False)

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

with app.app_context():
    db.create_all()

@click.command('init-db')
def init():
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_sample()
    click.echo('Database has been initialized.')

app.cli.add_command(init)

@click.command('import-genres')
@click.argument('path')
def import_genres(path):
    with app.app_context():
        db.create_all()
        added_main, added_sub = import_genres_from_json(path)
    click.echo(f'Import done: {added_main} main genres, {added_sub} subgenres.')

app.cli.add_command(import_genres)

def import_genres_from_json(path):
    with open(path, encoding='utf-8') as f:
        genre_map = json.load(f)

    added_main = 0
    added_sub = 0

    for main_name, sub_names in genre_map.items():
        main_genre = db.session.execute(
            db.select(MainGenre).filter_by(name=main_name)
        ).scalar()
        if main_genre is None:
            main_genre = MainGenre(name=main_name)
            db.session.add(main_genre)
            db.session.flush()
            added_main += 1

        for sub_name in sub_names:
            exists = db.session.execute(
                db.select(Subgenre).filter_by(name=sub_name, main_genre_id=main_genre.id)
            ).scalar()
            if exists is None:
                db.session.add(Subgenre(name=sub_name, main_genre_id=main_genre.id))
                added_sub += 1

    db.session.commit()
    return added_main, added_sub

def fetch_song(url,quiz_id, position):
        results = search_tracks(url, limit=1)
        if not results:
            return None
        t= format_track(results[0])
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
    # Delete all existing data, if any
    for model in [Score, Song, Quiz, Subgenre, MainGenre, User]:
        db.session.execute(db.delete(model))

    # Create sample users
    admin = User(username='admin', password_hash=hash_password('1234'), is_admin=True)
    user1 = User(username='BerlinPlayer', password_hash=hash_password('1234'), city='Berlin')
    user2 = User(username='ViennaPlayer', password_hash=hash_password('1234'), city='Vienna')

    # Create sample genres
    electronic = MainGenre(name='Electronic')
    jazz = MainGenre(name='Jazz')
    db.session.add_all([admin, user1, user2, electronic, jazz])
    db.session.commit()

    techno = Subgenre(name='Techno', main_genre_id=electronic.id)
    bebop = Subgenre(name='Bebop', main_genre_id=jazz.id)
    db.session.add_all([techno, bebop])
    db.session.commit()

    # Create sample quizzes
    quiz1 = Quiz(title='Electronic Starter', creator_id=admin.id, main_genre_id=electronic.id, subgenre_id=techno.id, difficulty='Easy')
    quiz2 = Quiz(title='Jazz Classics', creator_id=user1.id, main_genre_id=jazz.id, subgenre_id=bebop.id, difficulty='Medium')
    db.session.add_all([quiz1, quiz2])
    db.session.commit()

    # Create sample songs
    
    song_urls = [
         ('Deadmau5 Strobe',            quiz1.id, 1),
        ('Boys Noize Oi Oi Oi',        quiz1.id, 2),
        ('Dave Brubeck Take Five',     quiz2.id, 1),
        ('Frank Sinatra Fly Me to the Moon', quiz2.id, 2),
    ]
    
    songs = []
    for url, quiz_id, position in song_urls:
            song= fetch_song(url, quiz_id, position)
            if song:
                songs.append(song)

    # Create sample scores
    scores = [
        Score(user_id=user1.id, quiz_id=quiz1.id, points=150),
        Score(user_id=user2.id, quiz_id=quiz1.id, points=200),
    ]

    db.session.add_all(songs + scores)
    db.session.commit()
