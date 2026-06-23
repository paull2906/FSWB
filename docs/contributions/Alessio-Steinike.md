--- 
title: Alessio-Steinike
parent: Individual Contributions
nav_order: 3
--- 

Alessio Steinike
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
Verständnis und Umsetzung eines intuitiven Designs und UI; Vertiefung von Rollenaufgaben und Verteilungen in Projektgruppen
---
## Eidesstattliche Erklärung
**Alessio Steinike, Matrikelnr.: 77208590933**
Ich erkläre an Eides statt:
Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.
Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.
Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.
---
## Top-3 Contributions
| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Bestätigungsseite beim Quiz Löschen im Admin Panel implementiert (confirm_delete.html) | Es zeigt ein Sicherheitsbedenken, welches über eine Funktion löst, dadurch kann der Admin keien Quizze ausversehen löschen | Kein JavaScript erlaubt, daher musste die Lösung rein mit HTML, Jinja2 und Flask-Routen umgesetzt werden |
| 2 | Audio-Vorschau Feedback in play.html verbessert — fehlende Previews werden nun mit einem gelben Warning-Banner mit Icon angezeigt statt mit grauem Text  | Verbesserte User Experience — Spieler verstehen sofort warum kein Audio abspielbar ist | Lösung musste rein in Jinja2 und Bootstrap umgesetzt werden, da JavaScript verboten ist |
| 3 | Schwierigkeitsgrad in index.html, browse.html und play.html von Englisch auf Deutsch übersetzt.. | Konsistenz in der gesamten App — vorher war die UI gemischt Deutsch/Englisch | Alle drei Dateien mussten identisch angepasst werden ohne die Logik zu verändern |
## Design Decisions that I led
1. Bestätigungsseite für Quiz-Löschen (Sicherheitsverbesserung)-> Geänderte Dateien: admin.html, confirm_delete.html, app.py in eignener Arbeit.
2. Deutsch-Konsistenz und UX-Verbesserungen in HTML-Templates, -> Geänderte Dateien: index.html, browse.html, play.html, in eigener Arbeit
---
## Contributions
| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| UI-Wireframes für alle App-Screens erstellt | - | Eigene Arbeit |
| Value Proposition und Two-Sided Platform ausgearbeitet | [Assignment Re-Work](docs/assignment.md) | Claude (Anthropic) |
| Creator-Motivation-System konzipiert (Badge-System, Geo-Rankings) | [Assignment Re-Work](docs/assignment.md) | Claude (Anthropic) |
---
## AI Directory
| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Claude (Anthropic) | Überarbeitung der Value Proposition und Two-Sided Platform Argumentation nach Dozentenrückmeldung | Assignment Re-Work, Abschnitt Value Proposition und Two-Sided Platform | Dozentenrückmeldung und bestehenden Dokumentenstand eingegeben; Ergebnis geprüft und eigenständig eingearbeitet |
| 02  | Claude (Anthropic) | Ideenfindung Creator-Motivation-System (Badge-Konzepte, Geo-Ranking-Logik, Reputation-Score) | Assignment Re-Work, Abschnitt Creator-Motivation-System | Konzeptionellen Input als Ausgangspunkt genutzt; finale Ausgestaltung eigenständig entschieden |
| 03  |         |                |                                 |                             |
