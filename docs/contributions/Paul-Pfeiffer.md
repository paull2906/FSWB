---
title: Paul-Pfeiffer
parent: Individual Contributions
nav_order: 1
---

# Paul Pfeiffer

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

 1,7

### Personal goals

+ Sicherer Umgang mit APIs
+ Umsetzung einer App mit Frontend und Backend
+ Sicherer Umgang in der Dokumentationen von (Programmier-)Projekten

---

## Eidesstattliche Erklärung

**Paul Pfeiffer, Matrikelnr.: 77203983024**

Ich erkläre an Eides statt:
Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.
Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.
Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | [Describe your individual contribution] |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Design Decisions that I led

1. SQLAlchemy
2. Genre_logic
3. DB-SQLite_vs_Hosting 

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Repository erstellt | - | [HWR Berlin: FSWB](https://hwrberlin.github.io/fswd/git.html) |
| GitHub Pages erstellt | [Pages](https://paull2906.github.io/Musik-Quiz/) | [HWR Berlin: FSWB](https://hwrberlin.github.io/fswd/git.html)  |
| 02-Data-Model entwickelt | [02-Data-Model](https://github.com/paull2906/Musik-Quiz/blob/09fec4f2f44066ef569332297981ba74984fefd7/docs/02-data-model.md) | Gemini(Google) (1) |
| Design Decision: SQLAlchemy| [Design Decision: SQLAlchemy.md](https://github.com/paull2906/Musik-Quiz/blob/e4638a46008706adf03c37b279eb9453c4071847/docs/Design%20Decisions/SQLAlchemy.md)| [HWR Berlin: FSWB](https://hwrberlin.github.io/fswd/git.html), Claude(1)|
|db.py aufgebaut| [DB.py](https://github.com/paull2906/Musik-Quiz/blob/09fec4f2f44066ef569332297981ba74984fefd7/db.py) |  [HWR Berlin: FSWB](https://hwrberlin.github.io/fswd/git.html), [fswd-app](https://github.com/hwrberlin/fswd-app.git)|
| Design Decision: Genre_logic| [Design Desicion: Genre_logic](https://github.com/paull2906/Musik-Quiz/blob/0b8ee94f3185f22b1584854a77010cdaba15fef2/docs/Design%20Decisions/Genre_logic.md)| Feedback aus dem Peer-review |
|Design Decision: DB-SQLite_vs_Hosting | [Design Decision: DB-SQLite_vs_Hosting](https://github.com/paull2906/Musik-Quiz/blob/09fec4f2f44066ef569332297981ba74984fefd7/docs/Design%20Decisions/DB-SQLite_vs_Hosting.md)| [fswd-app](https://github.com/hwrberlin/fswd-app.git),[What is PostegreSQL](https://www.postgresql.org/about/)|

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Gemini (Google) (1)| Fehlerbehebung bei Markdown-Rendering-Fehlern im GitHub-Repository | Mermaid-Syntax in 02-Data-Models |Fehlerhafte Mermaid-Syntax-Fehlermeldung eingegeben. KI identifizierte fehlende Zeilenumbrüche und fälschlicherweise maskierte Backticks|
| 02  |Claude|Inhalte für Genres.json erstellen|[Genres.json](https://github.com/paull2906/Musik-Quiz/blob/09fec4f2f44066ef569332297981ba74984fefd7/genres.json)|Claude erstellte eine Liste an Genre Namen mit passenden Subgenres|
| 03 |Claude(1)|Gegenüberstellung SQLAlchemy und SQL zum Vergleich| [Design Decision: SQLAlchemy.md](https://github.com/paull2906/Musik-Quiz/blob/e4638a46008706adf03c37b279eb9453c4071847/docs/Design%20Decisions/SQLAlchemy.md), Indirekter Effekt auf [DB.py](https://github.com/paull2906/Musik-Quiz/blob/09fec4f2f44066ef569332297981ba74984fefd7/db.py), da es uns bei der Entscheidung unterstützt hat|Wir haben Claude genutzt um einen übersichtlichen Vergleich von SQL und SQAlchemy erstellen zu lassen, das unsere Entscheidung unterstützen sollte|  
