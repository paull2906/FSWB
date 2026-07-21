---
title: Home
nav_order: 0
---


# Musikquiz: Beat The Track
## By LiveRecords

Beat-The-Track ist eine Flask-basierte Web-App, in der User Musik-Quizze spielen und erstellen und spielen können. Pro Frage wird wird eine 30 sekündige Vorschau des zu erratenen Songs abgespielt, bei der dem der Player dann Titel und Interpret erraten soll. Erreichte Punktzahlen werden gespeichert und in einem Leaderboard für alle sichtbar gemacht.

## Sample App Screen



---

## Improvements / Refinements since First Submission

In app.py wurde die Funktion is_close_enough() verändert. Zum einen wurde eine Eingabe, die nur aus Leerzeichen besteht, vorher fälschlicherweise als richtige Antwort gewertet, was durch eine zusätzliche Prüfung direkt nach dem Entfernen der Leerzeichen behoben wurde. Zum anderen konnte man vorher mit der Eingabe eines einzelnen häufigen Buchstabens wie „e" fast jeden Songtitel als richtig geraten durchgehen lassen, da der Teilstring-Vergleich keine Mindestlänge hatte; das wurde durch eine neue Konstante MIN_SUBSTRING_LEN = 3 gefixt, die den Teilstring-Shortcut erst ab drei Zeichen greifen lässt.

In der Genres.json datei wurden noch zusätzliche deutsche Sub-Genres hinzugefügt, da wir bei der erstellung von Quizzen festgestellt haben, dass in dieser Richtung relativ wenig Möglichkeiten herrschten und wir da die Optionen der User vermehren wollten. 

Desweiteren wurde auch eine Design Decision für Bootstrap hinzugefügt. Zwar war Bootstrap bereits bestndteil unseres Codes, allerdings haben wir bislang keine Design Decision erstellt, die den Gedankengang hinter der Implementierung dargestellt hat.


{: .fs-2 }
Last build: {{ site.time | date: '%d %b %Y, %R%:z' }}
