---
title: Nutzung von WTForms
parent: Design Decisions
---

{: .no_toc }
# Formularverarbeitung – Manuelle HTML-Formulare vs. WTForms

## Meta

Status
: **Work in progress**

Updated
: 17.06.2026
---
## Problem Statement

Die zu treffende Entscheidung betrifft die Wahl der Methode zur Verarbeitung und Validierung von Formularen in der Web-App. Zur Auswahl stehen manuell implementierte HTML-Formulare und WTForms, eine Python-Bibliothek zur strukturierten Formularverarbeitung.
 
WTForms ermöglicht es, Formulare als Python-Klassen zu definieren und Validierungslogik zentral zu bündeln, ohne diese direkt im HTML oder in den Route-Funktionen implementieren zu müssen. Manuelle HTML-Formulare hingegen erfordern keine zusätzliche Bibliothek, da Eingaben direkt über "request.form" in Flask verarbeitet werden.
 
WTForms ist keinem aus der Gruppe bisher bekannt und müsste neu erlernt werden. Manuelle HTML-Formulare wurden im Rahmen des Studiums bereits behandelt und sind der Gruppe vertraut. Da die Implementierung der Formulare Alessio Steinicke zugeordnet worden ist, trägt er auch die Verantwortung für diese Entscheidung. An der Abwägung und Diskussion ist jedoch das gesamte Team beteiligt.
--- 
## Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

## Regarded Options

### Option A: Manuelle HTML-Formulare
 
Formulare werden als einfache HTML-Elemente implementiert, Eingaben werden direkt über "request.form" in Flask verarbeitet und manuell validiert.
 
| # | Pro | Contra |
|---|-----|--------|
| 1 | Keine zusätzliche Bibliothek notwendig | Validierungslogik muss für jedes Formular manuell und wiederholt implementiert werden |
| 2 | HTML-Formulare sind der Gruppe bereits zum Teil bekannt | Der Code wird bei mehreren Formularen schnell unübersichtlich |
| 3 | Direkter und nachvollziehbarer Datenfluss über "request.form" | Fehlerbehandlung und Nutzerfeedback müssen vollständig selbst umgesetzt werden |
 
---
 
### Option B: WTForms
 
Formulare werden als Python-Klassen mit integrierter Validierung über die Bibliothek WTForms definiert.
 
| # | Pro | Contra |
|---|-----|--------|
| 1 | Validierungslogik ist zentral in der Formularklasse gebündelt und muss nicht wiederholt werden | WTForms ist keinem aus der Gruppe bekannt und muss neu erlernt werden |
| 2 | Integrierte Validatoren (z. B. für Pflichtfelder, E-Mail-Format) reduzieren den Code erheblich | Das Einarbeiten nimmt anfänglich Zeit in Anspruch |
| 3 | Formulare sind als Python-Objekte wiederverwendbar und einfacher testbar | Die Fehleranfälligkeit ist initial erhöht, da keine Erfahrung mit WTForms vorhanden ist |
| 4 | Trennung der Logik der Formuaren sowie Routen verbessern die Übersichtlichkeit der App | |
 
