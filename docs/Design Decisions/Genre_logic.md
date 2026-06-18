---
title: Genre-Logik
parent: Design Decisions
---

{: .no_toc }
# [Klassifizierung der Genres bei Quizerstellung]

## Meta

Status
: **Decided** 

Updated
: 18-June-2026

## Problem Statement

Die Music-Quiz-Web-App ermöglicht es jedem Nutzer, Quizze zu nischigen Musikrichtungen zu erstellen und zu veröffentlichen. Dabei entsteht jedoch eine wichtige UX-Herausforderung bei der Klassifizierung der Genre während der Quiz-Erstellung. 
Die App soll das Alleinstellungsmerkmal haben, dass keine Musik-Quiz-App Quizze für spezifische Communitys und Genres abdeckt. Eine Liste mit den klassischsten Genres reicht daher nicht aus um diesem Merkmal gerecht zu werden. Ein freies Textfeld wo User das Genre einfach reinschrieben können würde zu Strukturlosigkeit und inkosistenz führen. 
Das Genre-System muss sowohl Browsing bzw. Filterung unterstützen, als auch Umfangreich sein, um genug Genres abzudecken. Gleichzeitig muss es jedoch übersichtlich bleiben.

## Decision

Wir haben uns für eine erweiterte Liste an Genres entschieden. 
Im Repository haben wir eine Genres.json datei angelegt und diese wie folgt befüllt: 
Zum einen sind die Hauptgenres augelistet. Pro Zeile ist ein Hauptgenre. Darauf folgen innerhalb der Klammer sogenannte Subgenres, die das Hauptgenre spezifischer abgrenzen. 
Subgenres wird per Texteingabe mit Autocomplete-Vorschlägen aus bereits verwendeten Subgenres eingetragen. Nutzer können auch völlig neue Subgenres frei eingeben. Werden Subgenres häufig benutzt werden sie manuell in die genres.json Datei hinzugefügt.
Die Entscheidung wurde in ganzen Team getroffen und wurde von Herrn Ecks Vorschlag aus den peer reviews beeinflusst.

## Regarded Options

- Hauptgenres bilden stabile Ankerpunkte für die Filterung und Browsing
- Subgenres sind der eigentliche Ort für Nischenspezifität, wobei eine freie Eingabe die Plattform offen hält
- Autocomplete bei Subgenres soll Duplikate verhindern
- Häufig verwendete freie Subgenres können von Admins in die `genres.json` aufgenommen werden
---
 
## Betrachtete Optionen
 
### Option A — Vollständig freie Texteingabe
 
Nutzer geben sowohl Genre als auch Subgenre vollständig frei ein.
 
| # | Pro | Contra |
|---|-----|--------| 
|1|Maximale kreative Freiheit|Hohes Duplikationsrisiko |
|2|Kein Wartungsaufwand für Genre-Listen|Filterung und Browsing werden unzuverlässig oder unmöglich| 
|3||Such-UX verschlechtert sich mit wachsendem Datenbestand|
|4||Keine konsitentes Bezeichnungen für die Genres|
 
---
 
### Option B — Feste geschlossene Liste
 
Eine einzelne, flache Genre-Liste als `.txt`-Datei im Repository. Quiz-Creator können nur aus dieser Liste auswählen.
 
| # | Pro | Contra |
|---|-----|--------| 
|1|Vollständig konsistente Daten|Widerspricht dem Nischen-Grundsatz der App|
|2|Einfach zu implementieren|Nutzer werden gehindert, legitime Nischen-Genres zu vergeben| 
|3|Einfach zu filtern und anzuzeigen|Aktualisierungen erfordern eine Code-Änderung|
|4||Eine flache Liste kann die hierarchische Natur von Genres nicht abbilden|


---
 
### Option C — Feste Hauptgenres + Offene Subgenres mit Autocomplete  (Gewählt)
 
Hauptgenres werden aus einem kuratierten Dropdown ausgewählt. Subgenres werden frei eingegeben, erhalten aber Vorschläge aus vorhandenen Daten.
 
| # | Pro | Contra |
|---|-----|--------| 
|1|Hauptgenres liefern konsistente, filterbare Struktur|Etwas aufwändiger zu implementieren als eine flache Liste|
|2|Subgenres ermöglichen beliebig nischige Klassifizierungen|Subgenre-Daten werden mit der Zeit etwas Rauschen ansammeln|
|3|Autocomplete reduziert Duplikate, ohne sie zu erzwingen|Erfordert periodische Kuratierung populärer Subgenres in den Vorschlagspool|
|4|Zweistufige Hierarchie ist intuitiv||
 
---