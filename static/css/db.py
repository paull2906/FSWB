import hashlib
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
    genre = db.Column(db.String(120), nullable=True)
    difficulty = db.Column(db.String(120), nullable=True)

    creator = db.relationship('User', back_populates='quizzes')
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

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', back_populates='scores')
    quiz = db.relationship('Quiz', back_populates='scores')
