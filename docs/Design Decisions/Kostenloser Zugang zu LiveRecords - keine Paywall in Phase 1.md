---
title: Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1
parent: Design Decisions
---

{: .no_toc }
# Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1

## Meta

Status
: Decided

Updated
: 18-Mai-2026

## Problem Statement

Da LiveRecords eine zweiseitige Plattform ist, benötigt sie das Zusammenspiel zweier Nutzergruppen: Creator und Player. Beide Seiten sind voneinander abhängig, denn ohne genug Player gibt es keine Motivation für Creator, Quizze zu erstellen und ohne genug Creator-Content gibt es nichts zu spielen. Wir befürchten, dass wir mit einer Paywall die Adoptionsschwelle erhöhen würden und riskieren könnten, dass weder genug Creator noch Player in ausreichender Zahl beitreten. Damit könnte die Plattform keinen Wert generieren, bevor sie überhaupt gestartet ist.

## Decision

LiveRecords wird in Phase 1 vollständig kostenlos und ohne Paywall angeboten. Alle Kernfunktionen, Quiz spielen, Quiz erstellen, Leaderboards einsehen, Creator-Profil aufbauen, sind ohne Bezahlung zugänglich. Monetarisierung und Premium-Features sind explizit als Out-of-Scope für Phase 1 definiert und auf Phase 2 verschoben. Diese Entscheidung wurde gemeinsam vom Team getroffen 

## Regarded Options

Option A: Vollständig kostenlos (gewählte Option)

Das gesamte Produkt ist ohne Paywall nutzbar. 
Pro:

- Maximiert die Chance, beide Seiten der Plattform gleichzeitig zu aktivieren — entscheidend für den Cross-Side-    Netzwerkeffekt (mehr Creator -> mehr Content -> mehr Player -> mehr Plays -> mehr Creator-Motivation)
- Senkt die Adoptionsschwelle auf null; der einzige "Preis" ist die Zeit für Quiz-Erstellung bzw. das Spielen
- Das Creator-Motivation-System (Geo-Rankings, Badges, Reputation-Score) funktioniert nur, wenn genug Player vorhanden sind, eine Paywall auf Player-Seite würde diesen Anreiz aushöhlen

Con:

- Kein direkter Umsatz in Phase 1


Option B: Freemium — Spielen kostenlos, Erstellen kostenpflichtig

Player können kostenlos spielen, Creator zahlen für den Zugang zum Quiz-Builder.
Pro: 

- Frühzeitige Monetarisierung auf Creator-Seite

Con:

- Zerstört den First-Mover-Anreiz: Ein Creator, der für das Erstellen zahlen muss, bevor er weiß, ob überhaupt Player kommen, hat kaum Motivation einzusteigen
- Verschärft das Cold-Start-Problem auf der Content-Seite massiv — ohne Creator kein Content, ohne Content keine Player


Option C: Freemium — Erstellen kostenlos, erweiterte Leaderboard-Features kostenpflichtig

Geo-Rankings oder bestimmte Statistiken nur für zahlende Nutzer.
Pro: 

- Monetarisierungspfad bei gleichzeitiger Basisnutzung

Con:

- Die Leaderboards und der Reputation-Score sind der zentrale Wertmechanismus für Creator, sie hinter einer Paywall zu verstecken würde bedeuten, den Hauptanreiz zur Quiz-Erstellung zu entfernen
- Eine fragmentierte Erfahrung schadet der Viralität: Share-Links, die nur für zahlende User vollständig funktionieren, reduzieren den Community-Spread 


