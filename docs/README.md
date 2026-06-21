# Musikquiz: Beat The Track
## By LiveRecords

Beat-The-Track ist eine Flask-basierte Web-App, in der User Musik-Quizze spielen und erstellen und spielen können. Pro Frage wird wird eine 30 sekündige Vorschau des zu erratenen Songs abgespielt, bei der dem der Player dann Titel und Interpret erraten soll. Erreichte Punktzahlen werden gespeichert und in einem Leaderboard für alle sichtbar gemacht.

## Funktionen
 
- Registrierung und Login mit gehashten Passwörtern (SHA-256)
- Quiz-Erstellung durch Nutzer ("Creator"), zugeordnet zu Haupt- und Subgenre
- Audio-Previews der Songs über die iTunes Search API (kein API-Key nötig)
- Punkte-/Score-System pro Quiz als Grundlage für Highscores
- Admin-Account zur Verwaltung
- Genre-Verwaltung (Hauptgenres + Subgenres), per CLI aus JSON importierbar

## Test-Zugänge
 
| Benutzername  | Passwort | Rolle          |
| ------------- | -------- | ---------------------- |
| `admin`       | `1234`   | Administrator          |
| `BerlinPlayer`| `1234`   | Player/ Creator        |
| `ViennaPlayer`| `1234`   | Player/ Creator       |
 
> Diese Zugänge dienen ausschließlich zu Testzwecken 

## Projektstruktur
 
```
Musik-Quiz/
├── app.py            # Flask-App, Konfiguration (SECRET_KEY), Routen
├── db.py             # SQLAlchemy-Modelle, init-db / import-genres CLI, Beispieldaten
├── forms.py          # Flask-WTF Formulare (Register, Login, CreateQuiz)
├── requirements.txt  # Abhängigkeiten
├── templates/        # Jinja2-Templates (z. B. quiz.html)
└── static/           # CSS / JS
```

## Installation und Start der App:
```bash
#1. Repository klonen
   git clone https://github.com/paull2906/Musik-Quiz.git
#2. Virtuelle Umgebung anlegen und aktivieren
   python -m venv venv
   source venv/bin/activate      #windows: venv\Scripts\activate
#3. Requirements in die virtuelle Umgebung laden
   pip install -r requirements.txt
#4. Web App starten
   python app.py  
```

