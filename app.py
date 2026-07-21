from pathlib import Path
from difflib import SequenceMatcher
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_wtf import CSRFProtect
import forms
app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment'
)
CSRFProtect(app) 

from db import db, User, Quiz, Song, MainGenre, Subgenre, Score, hash_password
from itunes import format_track, search_tracks

MIN_SUBSTRING_LEN = 3

def is_close_enough(guess, correct):
    if not guess:
        return False
    g = guess.lower().strip()
    if not g:
        return False
    c = correct.lower().strip()
    if len(g) >= MIN_SUBSTRING_LEN and (g in c or c in g):
        return True
    return SequenceMatcher(None, g, c).ratio() >= 0.75


def get_session_user():
    return session.get('user')


@app.route("/")
def index():
    return redirect(url_for('login'))


@app.route("/about")
def about():
    return "This is a Music Quiz App!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data

        existing_user = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalars().first()
        
        if existing_user:
            flash('Dieser Benutzername ist bereits vergeben.', 'warning')
            return render_template('register-window.html', form=form)

        new_user = User(
            username=username,
            password_hash=hash_password(password), 
            city=form.city.data.strip() if form.city.data else None,
            is_admin=False 
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Konto erfolgreich erstellt! Du kannst dich jetzt anmelden.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register-window.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data
        
        u = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalars().first()

        if u and u.password_hash == hash_password(password): 
            session['user'] = {'id': u.id, 'username': u.username, 'is_admin': u.is_admin, 'city': u.city}
            flash(f'Willkommen zurück, {u.username}!', 'success')
            return redirect(url_for('browse')) 
            
        flash('Ungültiger Benutzername oder Passwort.', 'danger')
        
    return render_template('login-window.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('Du wurdest abgemeldet.', 'info')
    return redirect(url_for('index'))


@app.route('/browse')
def browse():
    user = get_session_user()
    main_genre_id = request.args.get('main_genre_id', type=int)
    query = db.select(Quiz)
    if main_genre_id:
        query = query.filter_by(main_genre_id=main_genre_id)
    query = query.order_by(Quiz.id.desc())
    quizzes = db.session.execute(query).scalars().all()
    main_genres = db.session.execute(db.select(MainGenre)).scalars().all()
    return render_template('browse.html', user=user, quizzes=quizzes,
                            main_genres=main_genres, selected_main_genre_id=main_genre_id)


@app.route('/create', methods=['GET', 'POST'])
def create():
    user = get_session_user()
    if not user:
        flash('Bitte melde dich an.', 'warning')
        return redirect(url_for('login'))
        
    if request.method == 'GET':
        session['staged'] = []

    staged = session.get('staged', [])
    search_results = []
    title = request.form.get('title', '')
    main_genre_id = request.form.get('main_genre_id', '')
    subgenre_id = request.form.get('subgenre_id', '')
    difficulty = request.form.get('difficulty', 'Medium')
    search_query = request.form.get('search_query', '')

    if request.method == 'POST':
        if 'do_search' in request.form:
            
            if search_query:
                try:
                    raw = search_tracks(search_query)
                    search_results = [format_track(t) for t in raw]
                except Exception:
                    flash('iTunes-Suche fehlgeschlagen. Bitte später erneut versuchen.', 'danger')
        elif 'add_idx' in request.form:

            idx = request.form['add_idx']
            song = request.form.get(f'res_title_{idx}')
            if song:
                staged.append({
                    'itunes_id': request.form.get(f'res_id_{idx}', ''),
                    'title': song,
                    'artist': request.form.get(f'res_artist_{idx}', ''),
                    'album': request.form.get(f'res_album_{idx}', ''),
                    'preview_url': request.form.get(f'res_preview_{idx}', ''),
                    'cover_url': request.form.get(f'res_cover_{idx}', ''),
                })
                session['staged'] = staged
        elif 'remove_idx' in request.form:
           
            idx = int(request.form['remove_idx'])
            if 0 <= idx < len(staged):
                staged.pop(idx)
                session['staged'] = staged
        elif 'do_save' in request.form:
        
            if not title or not main_genre_id:
                flash('Titel und Hauptgenre sind erforderlich.', 'danger')
            elif len(staged) < 2:
                flash('Ein Quiz benötigt mindestens 2 Songs.', 'danger')
            else:
                quiz = Quiz(creator_id=user['id'], title=title,
                            main_genre_id=int(main_genre_id),
                            subgenre_id=int(subgenre_id) if subgenre_id else None,
                            difficulty=difficulty)
                db.session.add(quiz)
                db.session.flush()
                position = 1
                for s in staged:
                    db.session.add(Song(
                        quiz_id=quiz.id, itunes_id=s['itunes_id'], title=s['title'],
                        artist=s['artist'], album=s['album'], preview_url=s['preview_url'],
                        cover_url=s['cover_url'], position=position,
                    ))
                    position += 1
                db.session.commit()
                session.pop('staged', None)
                flash('Quiz erfolgreich erstellt!', 'success')
                return redirect(url_for('browse'))

    main_genres = db.session.execute(db.select(MainGenre)).scalars().all()

    if main_genre_id:
        subgenres = db.session.execute(
            db.select(Subgenre).filter_by(main_genre_id=int(main_genre_id))
        ).scalars().all()
    else:
        subgenres = []

    return render_template('create.html', user=user, staged=staged,
                            search_results=search_results, search_query=search_query,
                            title=title, main_genres=main_genres, subgenres=subgenres,
                            main_genre_id=main_genre_id, subgenre_id=subgenre_id,
                            difficulty=difficulty)


@app.route('/play/<int:quiz_id>', methods=['GET', 'POST'])
def play(quiz_id):
    user = get_session_user()
    if not user:
        flash('Bitte melde dich an, um zu spielen.', 'warning')
        return redirect(url_for('login'))
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz:
        flash('Quiz nicht gefunden.', 'danger')
        return redirect(url_for('browse'))

    if request.method == 'POST':
        total = 0
        results = []
        for song in quiz.songs:
            guess_title = request.form.get(f'title_{song.id}', '')
            guess_artist = request.form.get(f'artist_{song.id}', '')
            title_ok = is_close_enough(guess_title, song.title)
            artist_ok = is_close_enough(guess_artist, song.artist)

            points = 0
            if title_ok:
                points += 100
            if artist_ok:
                points += 50

            total += points
            results.append({
                'title': song.title, 'artist': song.artist, 'album': song.album,
                'cover_url': song.cover_url, 'guess_title': guess_title,
                'guess_artist': guess_artist, 'title_ok': title_ok,
                'artist_ok': artist_ok, 'points': points,
            })
        score = Score(user_id=user['id'], quiz_id=quiz.id, points=total)
        db.session.add(score)
        db.session.commit()
        session['last_results'] = results
        return redirect(url_for('result', quiz_id=quiz.id, points=total))

    return render_template('play.html', user=user, quiz=quiz)


@app.route('/result/<int:quiz_id>')
def result(quiz_id):
    user = get_session_user()
    if not user:
        flash('Bitte melde dich an.', 'warning')
        return redirect(url_for('login'))
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz:
        flash('Quiz nicht gefunden.', 'danger')
        return redirect(url_for('browse'))

    points = int(request.args.get('points', 0))
    results = session.get('last_results', [])

    all_scores = db.session.execute(
        db.select(Score).filter_by(quiz_id=quiz.id)
    ).scalars().all()

    player_ids = []
    for s in all_scores:
        if s.user_id not in player_ids:
            player_ids.append(s.user_id)
    total_players = len(player_ids)
    if total_players == 0:
        total_players = 1
        
    rank = 1
    for s in all_scores:
        if s.points > points:
            rank += 1

    return render_template('result.html', user=user, quiz=quiz, points=points,
                            rank=rank, total_players=total_players, results=results)


@app.route('/leaderboard/<int:quiz_id>')
def leaderboard(quiz_id):
    user = get_session_user()
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz:
        flash('Quiz nicht gefunden.', 'danger')
        return redirect(url_for('browse'))

    city = request.args.get('city', '')

    all_scores = db.session.execute(
        db.select(Score).filter_by(quiz_id=quiz_id)
    ).scalars().all()

    best_scores = {}
    for s in all_scores:
        if s.user_id not in best_scores or s.points > best_scores[s.user_id]:
            best_scores[s.user_id] = s.points

    entries = []
    cities = []
    for user_id, best_score in best_scores.items():
        player = db.session.get(User, user_id)
        if player.city and player.city not in cities:
            cities.append(player.city)
        if city and player.city != city:
            continue
        entries.append({
            'id': player.id,
            'username': player.username,
            'city': player.city,
            'best_score': best_score,
        })

    entries.sort(key=lambda e: e['best_score'], reverse=True)

    return render_template('leaderboard.html', user=user, quiz=quiz, entries=entries,
                            cities=cities, selected_city=city)

@app.route('/admin/confirm-delete/<int:quiz_id>')
def confirm_delete(quiz_id):
    user = get_session_user()
    if not user or not user['is_admin']:
        flash('Nur für Admins.', 'danger')
        return redirect(url_for('index'))
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz:
        flash('Quiz nicht gefunden.', 'danger')
        return redirect(url_for('admin'))
    return render_template('confirm_delete.html', user=user, quiz=quiz)
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    user = get_session_user()
    if not user or not user['is_admin']:
        flash('Nur für Admins.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'delete_quiz':
            quiz_id = int(request.form.get('quiz_id'))
            quiz = db.session.get(Quiz, quiz_id)
            if quiz:
                db.session.delete(quiz)
                db.session.commit()
                flash('Quiz gelöscht.', 'success')

    users = db.session.execute(db.select(User)).scalars().all()
    quizzes = db.session.execute(db.select(Quiz)).scalars().all()
    return render_template('admin.html', user=user, users=users, quizzes=quizzes)


@app.route('/api/quizzes')
def api_quizzes():
    quizzes = db.session.execute(db.select(Quiz)).scalars().all()
    return jsonify([{
        'id': q.id, 'title': q.title,
        'genre': q.main_genre.name if q.main_genre else None,
        'difficulty': q.difficulty,
        'creator': q.creator.username, 'songs': len(q.songs),
    } for q in quizzes])


@app.route('/api/leaderboard/<int:quiz_id>')
def api_leaderboard(quiz_id):
    quiz = db.session.get(Quiz, quiz_id)
    if not quiz:
        return jsonify({'error': 'not found'}), 404

    all_scores = db.session.execute(
        db.select(Score).filter_by(quiz_id=quiz_id)
    ).scalars().all()

    best_scores = {}
    for s in all_scores:
        if s.user_id not in best_scores or s.points > best_scores[s.user_id]:
            best_scores[s.user_id] = s.points

    entries = []
    for user_id, best_score in best_scores.items():
        player = db.session.get(User, user_id)
        entries.append({'username': player.username, 'city': player.city, 'best_score': best_score})

    entries.sort(key=lambda e: e['best_score'], reverse=True)

    return jsonify({
        'quiz': {'id': quiz.id, 'title': quiz.title,
                 'genre': quiz.main_genre.name if quiz.main_genre else None},
        'entries': entries,
    })


@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
