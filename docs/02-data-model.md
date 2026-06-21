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
   
    USER ||--o{ QUIZ : creates
    USER ||--o{ SCORE : achieves
    QUIZ ||--o{ SONG : contains
    QUIZ ||--o{ SCORE : has
    MAIN_GENRE ||--o{ SUBGENRE : has
    MAIN_GENRE |o--o{ QUIZ : categorizes
    SUBGENRE |o--o{ QUIZ : categorizes
    
    
    USER {
        int user_id PK
        string username
        boolean is_admin
        string password_hash
        string city
        }

    QUIZ {
        int quiz_id PK
        string title
        string description
        int creator_id FK
        int main_genre_id FK
        int subgenre_id FK
        string difficulty
      }

   
    SONG {
        int song_id PK
        int quiz_id FK
        string itunes_id
        string title
        string album
        string artist
        string preview_url
        string cover_url
        int position
    }

    MAINGENRE {
        int maingenre_id PK
        string name 
    }

    SUBGENRE {
        int id PK
        string name
        int main_genre_id FK
    }

    SCORE {
        int id PK
        int user_id FK
        int quiz_id FK
        int points
    }
```

#### 1. Entities und Attribute
* **User:** Speichert die Account-Daten, sowie eine Authentifizierung (gehashte Passwörter)
* **Quiz:** Speichert die von Creatoren erstellten Quiz-Pakete mit Bezug zu einem Genre und dem Schwierigkeitslevel
* **Maingenre:** Enthält alle gängigen Oberkategorien als Liste um sie für die Quizbeschreibung zu nutzen
* **Subgenre:** Enthält spezifische Musikrichtungen als Unterkategorie des Maingenres
* **Score:** Speichert absteigend die User mit den höchsten Punktzahlen für ein bestimmtes Quiz
* **Song:** Der Song enthält alle Daten, die für die API mit Itunes notwendig sind, sowie die 30-Sekunden Vorschau und die Position der Songs im Quiz


#### 2. Relationen
* **User to Quiz (1:N):** Ein User kann als "Creator" mehrere Quizze erstellen. jedes Quiz gehört über `creator_id` immer genau einem User
* **Quiz to Score (1:N):** u jedem Quiz können viele Scores entstehen, jeder Score bezieht sich auf genau ein Quiz
* **Quiz to Song (1:N):** Ein Quiz enthält mehrere Songs, sortiert über das Feld `position`; jeder Song gehört zu genau einem Quiz
* **User to Score (1:N):** Ein User kann viele Scores erzielen, jeder Score gehört zu genau einem User
* **MainGenre to Subgenre (1:N):** Ein Hauptgenre kann mehrere Subgenres haben; jedes Subgenre gehört zu genau einem Hauptgenre
* **MainGenre to Quiz (1:N, optional):** Ein Quiz kann einem Hauptgenre zugeordnet sein
* **Subgenre to Quiz (1:N, optional):** Ein Quiz kann einem Subgenre zugeordnet sein

