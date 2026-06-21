from pathlib import Path
from flask import Flask, render_template, redirext, url_for, request, flash
import forms
from db import db, User, Quiz, Song, MainGenre, Subgenre, Score

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment'
)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/about")
def about():
    return "This is a Music Quiz App!"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/quiz/create', methods=['GET', 'POST'])
def create_quiz():
    form = forms.CreateQuizForm()
    main_genres = db.session.execute(db.select(MainGenre).order_by(MainGenre.name)).scalars()
    form.main_genre_id.choices = [(g.id, g.name) for g in main_genres]
    subgenres = db.session.execute(db.select(Subgenre).order_by(Subgenre.name)).scalars()
    form.subgenre_id.choices = [(s.id, s.name) for s in subgenres]

    if form.validate_on_submit():
        quiz = Quiz(
            title=form.title.data,
            main_genre_id=form.main_genre_id.data,
            subgenre_id=form.subgenre_id.data,
            difficulty=form.difficulty.data,
            creator_id=...,  # eingeloggter User
        )
        db.session.add(quiz)
        db.session.commit()
        flash('Quiz has been created.', 'success')
        return redirect(url_for('quizzes'))

    return render_template('create_quiz.html', form=form)




@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)

