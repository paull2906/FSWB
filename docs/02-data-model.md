---
title: Data Model
nav_order: 3
---

{: .no_toc }
# Data Model

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

```mermaid

erDiagram
    USER ||--o{ QUIZ_SESSION : plays
    USER ||--o{ LEADERBOARD : appears_in
    QUIZ ||--o{ QUIZ_SESSION : has
    QUIZ_SESSION ||--o{ QUIZ_ANSWER: contains
    USER ||--o{ QUIZ : creates
    QUIZ ||--o{ LEADERBOARD : has
    QUIZ ||--|{ QUESTION : contains
    QUIZ ||--|| GENRE : based_on
    TRACK ||--o{ QUESTION : based_on
    QUESTION ||--o{ QUIZ_ANSWER : answered_by
    
    
    USER {
        int user_id PK
        string username
        boolean is_admin
        string password_hash
        }

    QUIZ {
        int quiz_id PK
        string quiz_name
        string description
        string genre_id FK
        int user_id FK
        datetime created_at
      }

    QUIZ_SESSION {
        int session_id PK
        int quiz_id FK
        int user_id FK
        int score
    }

    TRACK {
        int track_id PK
        string title
        string artist
        string preview_url
    }

    GENRE {
        int genre_id PK
        string genre_name 
    }


    QUESTION {
        int question_id PK
        string correct_title
        string correct_artist
        int quiz_id FK
        int track_id FK
    }    

  QUIZ_ANSWER {
    int answer_id PK
    int session_id FK
    int question_id FK
    string user_answer_title
    string user_answer_artist
    boolean title_correct
    boolean artist_correct
}
```

#### 1. Entities und Attribute
* **User:** Speichert die Account-Daten, sowie eine Authentifizierung (gehashte Passwörter)
* **Quiz_Session:** Protokolliert jedes gespielte Spiel eines Nutzers mit dem finalen Score, um Highscores für das Leaderboard zu berechnen
* **Quiz_Answer:** Speichert die Antwort des Titels und Interpreten zu jeder einzelnen Frage innerhalb einer Session
* **Quiz:** Speichert die von Creatoren erstellten Quiz-Pakete mit Bezug zu einem Genre
* **Genre:** Enthält alle gängigen Genres als Liste um sie für die Quizbeschreibung zu nutzen
* **Leaderboard:** Speichert absteigend die User mit den höchsten Punktzahlen für ein bestimmtes Quiz
* **Question:** verknüpft einen Quiz-Eintrag mit einem Track. Das Feld question_type ermöglicht spätere Erweiterungen ohne Schemaänderung. position steuert die Reihenfolge der Fragen
* **Track:** Der Track speichert ausschließlich die spotify_track_id. Titel, Cover-Art und Audio-Preview werden zur Laufzeit live via Spotipy bezogen


#### 2. Relationen
* **User to Quiz_Session (1:N):** Ein User kann viele Quiz-Sessions spielen, aber eine Session gehört immer exakt zu einem User
* **Quiz_Session to Quiz_Answer (1:N):** In einer Quiz-Session können beliebig viele Antworten zum Titel und Interpreten des Songs abgeschickt werden
* **Quiz to Quiz_Session (1:N):** Zu jedem Quiz können Quiz-session entstehen
* **User to Quiz (1:N):** Ein User kann als "Creator" mehrere Quizze erstellen
* **Quiz to Leaderboard (1:N):** Pro Quiz kann es mehrere Einträge im Leaderboard geben
* **User to Leaderboard (1:N):** Ein User kann in mehreren Leaderboards gelistet sein
* **Track to Question (1:N):** Ein Track kann in mehreren Fragen vorkommen
* **Question to Quiz_Answer(1:N):** Eine Question kann mehrere Quiz_Answers zum Titel und Interpreten enthalten
* **Quiz to Question (1:N):** Ein Quiz muss mindestens eine Question enthalten
* **Quiz to Genre (1:1):** Ein Quiz ist immer an ein Genre gebunden


