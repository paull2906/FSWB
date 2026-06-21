---
title: SQLAlchemy
parent: Design Decisions
---
{: .no_toc }
# Datenbankzugriff – SQL vs. SQLAlchemy

## Meta

Status
: **Decided**

Updated
: 17.06.2026

---

## Problem Statement

Die zu treffende Entscheidung betrifft die Wahl der Methode für die Verwaltung der Datenbank. Zur Auswahl stehen reguläres SQL und SQLAlchemy. SQLAlchemy ist ein sogenanntes ORM-Framework (Object Relational Mapper), das es ermöglicht, Daten aus der Datenbank ohne direkte CRUD-Befehle zu verwalten.

SQLAlchemy kann den Umgang mit der Datenbank erleichtern und die Übersichtlichkeit im Code verbessern. Allerdings hat bisher niemand aus der Gruppe SQLAlchemy eingesetzt, weshalb ein Einarbeiten notwendig wäre. SQL hingegen wurde bereits mehrfach in Modulen des Studiums behandelt.

---

## Decision

In der App wird SQLAlchemy genutzt. Zum einen, um das Framework kennenzulernen und es gegebenenfalls für spätere Projekte einsetzen zu können. Außerdem erleichtert es den Umgang mit der Datenbank und verbessert die Übersichtlichkeit im Code deutlich.

Die von Herrn Eck bereitgestellte Dokumentation zu SQLAlchemy hat die Entscheidung maßgeblich beeinflusst: Sie konnte alle wichtigen Fragen und Unklarheiten klären, die sonst aufwändig hätten recherchiert werden müssen. Dies war eine wesentliche Hilfe und der ausschlaggebende Punkt für die Entscheidung zugunsten von SQLAlchemy.

Da die Initialisierung und Verwaltung der Datenbank Paul Pfeiffer zugeordnet worden sind, trägt er auch die Verantwortung für diese Entscheidung. An der Abwägung und Diskussion war jedoch das gesamte Team beteiligt.

---

## Regarded Options

### Option A: Reguläres SQL

Verwendung von standardmäßigem SQL für die Verwaltung der Datenbank.

| # | Pro | Contra |
|---|-----|--------|
| 1 | Die Abfragesprache wurde bereits intensiv im Kurs „Datenbanken" behandelt | CRUD-Befehle erfordern viel manuelles Schreiben |
| 2 | CRUD-Befehle können sicher angewendet werden | SQL-Code wird bei wachsender Komplexität schnell unübersichtlich |
| 3 | Die Logik hinter SQL ist tief verankert und muss nicht neu erlernt werden | Das manuelle Aufschreiben aller notwendigen CRUD-Befehle nimmt erheblich Zeit in Anspruch |

---

### Option B: SQLAlchemy (gewählte Option)

Verwendung von SQLAlchemy als ORM-Framework für die Verwaltung der Datenbank.

| # | Pro | Contra |
|---|-----|--------|
| 1 | CRUD-Befehle müssen nicht manuell geschrieben werden | SQLAlchemy ist keinem aus der Gruppe bekannt und muss neu erlernt werden |
| 2 | Modernerer Standard für Datenbankzugriff wird erlernt | Das Einarbeiten nimmt anfänglich Zeit in Anspruch |
| 3 | SQLAlchemy spart langfristig Zeit bei der Entwicklung | Die Fehleranfälligkeit ist initial erhöht, da keine Erfahrung mit SQLAlchemy vorhanden ist |
| 4 | Die Dokumentation von Herrn Eck steht als ausführliche Einführung zur Verfügung | |
