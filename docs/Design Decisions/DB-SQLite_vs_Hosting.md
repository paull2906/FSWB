---
title: Datenbank – SQLite vs. Hosting-Dienst
parent: Design Decisions
---

{: .no_toc }

# 05: Datenbank – SQLite vs. Hosting-Dienst

## Meta

Status
: Decided

Updated
: 21-Jun-2026

## Problem Statement

Die Anwendung verwendet derzeit eine lokale SQLite-Datei, wodurch der gesamte Datenbestand fest an das einzelne Gerät gebunden ist. Ein Quiz, das ein Teammitglied lokal anlegt, taucht bei den anderen nicht auf, weil jede laufende Instanz ihre eigene Datei führt. Von einem Admin erstellte Quizze können also nicht andere Spieler spielen. Auch die Musikvorschau wird nur lokal gespeichert. Zur Demonstration unserer App ist das ein Nachteil, da wir somit Sample-Daten in db.py aufwendig speichern müssen. Die Alternative ist ein Hosting-Dienst, bei dem wir den Datenbestand online speichern können. Dafür würden jedoch Gebühren anfallen. Zu klären ist nun, ob für Abgabe und Demonstration ein geräteübergreifend gemeinsamer Datenbestand erforderlich ist. Falls ja, muss geklärt werden, welcher Hosting-Dienst in Anspruch genommen wird.

## Decision

Wir haben uns dafür entschieden, bei SQLite zu bleiben. Somit sind alle Daten nur lokal gespeichert, Admins können aber Sample-Daten innerhalb des Codes deklarieren. Das nimmt uns zwar Flexibilität, erspart uns jedoch einen hohen Aufwand und mögliche Kosten. Zudem wird die Entscheidung legitimiert, da wir damit auch im Rahmen der Anforderungen von Herrn Eck bleiben. 

## Regarded Options

### Option A: Bei SQLite bleiben (gewählt)
Die App läuft weiterhin ausschließlich lokal Die Daten verbleiben lokal auf dem jeweiligen Rechner und es wird Sample-Data in db.py initialisiert.

| Pro | Contra |
| --- | --- |
| Kein zusätzliches Setup, keine Kosten, keine Accounts | Daten sind pro Gerät isoliert, es herrscht kein gemeinsamer Stand |
| Entspricht dem Stack der fswd-App | Von anderen Geräten nicht erreichbar |
| Für eine lokale Live-Demo bei der Abgabe ausreichend | Kein gemeinsames Arbeiten an realen Daten möglich |
| Man müsste keinen Hosting-Dienst suchen | Sample-Daten müssen umständlich manuell eingetragen werden|

### Option B: Zu Hosting-Dienst wechseln

Alle Daten werden online auf einer gehosteten Datenbank gespeichert. Somit sind erstellte Quizze für alle sichtbar und jeder kann sie spielen. Ein möglicher Hostinganbieter könnte PostgreSQL sein.

| Pro | Contra |
| --- | --- |
| Echte persistente, gemeinsam genutzte und nebenläufig sichere Datenbank | Höchster Aufwand: zusätzlicher Dienst, geänderte Konfiguration, evtl. Kosten |
| Ermöglicht eine flexiblere Demonstration der App | Nicht unbedingt in den Erwartungen des Dozenten gefordert |
| Produktionsnäher und besser skalierbar | |
