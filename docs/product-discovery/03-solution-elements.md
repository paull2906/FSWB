---
title: Solution Elements
parent: Product Discovery
nav_order: 3
---
{: .no_toc }
# Solution Elements

## Core Solution

LionRecords ist eine Web-App, auf der Quizmaster eigene Audio-Quizze erstellen und Player diese kompetitiv lösen können — mit persistenten Ranglisten auf Stadt-, Deutschland-, Europa- und Weltebene.

Die Spotify Web API liefert 30-Sekunden-Snippets für jeden Song, sodass keine eigene Audio-Lizenzierung notwendig ist.

---

## Solution Elements im Überblick

| # | Element | Beschreibung | Adressiert Problem |
| :-- | :-- | :-- | :-- |
| 1 | Spotify-gestützter Quiz-Builder | Songsuche via Spotify API, Selektion bis zu 15 Songs, Benennung und Veröffentlichung | Problem A |
| 2 | Game Interface mit Timer | 30s-Snippet, Countdown, Texteingabe, Punkte sinken mit der Zeit | Problem B |
| 3 | Persistentes Leaderboard pro Quiz | Rangliste bleibt über Spielrunden erhalten, Tabs: Diese Woche / Gesamt | Problem B |
| 4 | Geo-Ranglisten (Stadt / DE / EU / Global) | Geografisch gefilterte Rankings für Player und Creator | Problem B |
| 5 | Creator-Profil mit Reputation-Score | Öffentliches Profil mit Plays, Completion Rate, Badges, Genre-Ranking | Problem A |
| 6 | Badge-System für Creator | Automatisch vergebene Auszeichnungen (Genre Pioneer, City Champion, Unbeatable, ...) | Problem A |
| 7 | Genre-Leaderboard | Rangliste der besten Quizmaster pro Genre und geografischer Ebene | Problem A |
| 8 | Share-Link per Ergebnis | Teilbarer Link nach Spielende für Community-Challenges | Problem B |

---

## Value Proposition Canvas

### Für den Quizmaster (Creator)

**Jobs to be done:**
- Nischen-Wissen sichtbar machen
- Als Experte in der Community wahrgenommen werden
- Die Community herausfordern

**Pains:**
- Keine Audio-Quiz-Tools mit Nischen-Support
- Kein integriertes Publikum auf bestehenden Plattformen
- Aufwand steht nicht im Verhältnis zur Reichweite

**Gains:**
- Sichtbarkeit durch Creator-Profil und Genre-Ranking
- Badges als sozialer Beweis
- Engagement-Daten (Plays, Completion Rate) auf einen Blick

**Pain Relievers:** Quiz-Builder mit Spotify-Integration, sofortige Veröffentlichung, Creator-Profil  
**Gain Creators:** Badge-System, Geo-Rankings, Reputation-Score, Genre-Leaderboard

---

### Für den Player

**Jobs to be done:**
- Nischen-Wissen testen
- Sich mit anderen messen
- Ergebnisse in der Community teilen

**Pains:**
- Bestehende Apps testen nur Mainstream-Wissen
- Kein persistentes Leaderboard
- Kein teilbarer Ergebnis-Link

**Pain Relievers:** User-generated Nischen-Content, persistente Ranglisten, Share-Link  
**Gain Creators:** Geo-Filter (Stadt / DE / EU / Global), wöchentliche Rankings, kompetitive Dynamik

---

## [Raw Material]

### Screens

1. Home / Discovery
2. Quiz Creator Dashboard
3. Game Interface
4. Leaderboard (Quiz)
5. Creator-Profil
6. Genre-Leaderboard

### Technologie-Entscheidungen

| Layer | Technologie | Begründung |
| :-- | :-- | :-- |
| Frontend | React + Vite | Komponentenbasiert, schnelle Iteration |
| Backend | Node.js + Express | REST-API, leichtgewichtig |
| Datenbank | PostgreSQL | Relationales Modell, saubere Geo-Queries |
| Externe API | Spotify Web API | 30s-Preview-URLs, keine eigene Lizenzierung |
| Auth | Spotify OAuth 2.0 | SSO, User haben bereits einen Account |
