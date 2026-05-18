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
    USER ||--o{ LEADERBOARD : contains
    QUIZ_SESSION ||--o{ QUIZ_ANSWER : contains
    USER ||--o{ QUIZ : creates
    QUIZ ||--|| LEADERBOARD : has_unique
    
    USER {
        int user_id PK
        string username
        string email
        string password_hash
        int beat_coins_balance
        datetime created_at
        datetime updated_at
    }

    QUIZ {
        int quiz_id PK
        string quiz_name
        int total_songs
        string genre
        int user_id FK
        int username
        datetime created_at
        datetime updated_at

  }

    QUIZ_SESSION {
        int quiz_id FK
        int user_id FK
        int score
        int total_questions
        datetime played_at
    }

    QUIZ_ANSWER {
        int answer_id PK
        int session_id FK
        string spotify_track_id
        string user_choice
        boolean is_correct
    }

  LEADERBOARD {
        int ranking_position
        int user_id FK
        int quiz_id FK
        int score
        datetime played_at
        datetime updated_at
 }
```

#### 1. Entities & Attributes
* **User:** Speichert die Account-Daten, sowie eine Authentifizierung (gehashte Passwörter)
* **Quiz_Session:** Protokolliert jedes gespielte Spiel eines Nutzers mit dem finalen Score, um Highscores für das Leaderboard zu berechnen
* **Quiz_Answer:** Speichert die Antwort zu jeder einzelnen Frage innerhalb einer Session
* **Quiz:** Speichert die von Creatoren erstellten Quiz-Pakete mit Bezug zu einem Genre
* **Leaderboard:** Speichert absteigend die User mit den höchsten Punktzahlen für ein bestimmtes Quiz

#### 2. Relations (Beziehungen)
* **User to Quiz_Session (1:N):** Ein User kann viele Quiz-Sessions spielen, aber eine Session gehört immer exakt zu einem User
* **Quiz_Session to Quiz_Answer (1:N):** Eine Quiz-Session besteht aus mehreren beantworteten Fragen
* **User to Quiz (1:N):** Ein User kann als "Creator" mehrere Quizze erstellen
* **Quiz to Leaderboard (1:1):** Pro Quiz gibt es genau ein Leaderboard
* **User to Leaderboard (1:N):** Ein User kann in mehreren Leaderboards gelistet sein
