---
title: template
parent: Design Decisions
---

{: .no_toc }
# Anti-Cheat-Mechanismus für Scores

## Meta

Status
: Decided 

Updated
: 21-Jul-2026

## Problem Statement

Die Ergebnisseite zeigt nach jedem Spieldurchlauf für jeden Song den korrekten Titel und Interpreten, unabhängig davon, ob richtig geraten wurde.
Ein Spieler könnte ein Quiz absichtlich schlecht spielen, sich anschließend die korrekten Antworten auf der Ergebnisseite ansehen und das Quiz danach
erneut mit diesem Wissen spielen, um einen künstlich hohen Score im Leaderboard zu erzielen. Da leaderboard() und api_leaderboard() den besten Score 
pro Nutzer über alle Spieldurchläufe hinweg heranziehen, würde ein solcher zweiter Versuch den bisherigen Bestwert sofort überschreiben.

## Decision

Es wird in dieser Projektphase kein Anti-Cheat-Mechanismus umgesetzt.
Begründung: Beide im Detail geprüften Lösungsansätze haben Nachteile, die im Verhältnis zum tatsächlichen Risiko nicht gerechtfertigt sind. 
Eine wirksame, vollständige Lösung würde zusätzlich eine Überarbeitung der Ergebnisanzeige selbst erfordern (korrekte Antworten nicht sofort vollständig offenlegen),
was über den aktuellen Projektumfang hinausgeht  und da die App keine echten Wettbewerbs- oder Geldwerte abbildet, schätzen wir das Risiko als vertretbar ein.

Entschieden von: Leo Harnoth



## Regarded Options

Option A — Nur der erste Versuch zählt fürs Leaderboard

Pro: schließt die Lücke strukturell vollständig, unabhängig von Zeitpunkt oder Wiederholungen; einfache Umsetzung über ein zusätzliches Boolean-Feld auf Score.

Contra: nimmt Spielern jede zweite ehrliche Chance (z.B. bei Verbindungsabbruch mitten im ersten Versuch); fühlt sich für Nutzer ggf. unfair an.

Option B — Sperrfrist vor erneutem Spielen/Zählen

Pro: verhindert sofortiges Nachbessern, begrenzt Farmen auf maximal einen neuen Versuch für eine gewisse Zeitspanne.
Contra: löst das eigentliche Problem nachweislich nicht vollständig, da die Antworten sofort nach dem Spielen offengelegt werden, kann ein Nutzer die Sperrfrist
einfach abwarten und danach mit noch erinnertem Wissen einen geschönten Score einreichen. Außerdem würde das zusätzlichen Implementierungsaufwand ohne vollständige Absicherung bedeuten.

Option C — Keine Maßnahme, Risiko akzeptieren (gewählt)

Pro: keine zusätzliche Komplexität, keine Schema-Migration, keine UX-Reibung für ehrliche Spieler.
Contra: Leaderboard-Werte können von einem motivierten Nutzer manipuliert werden; akzeptiert, da keine echten Wettbewerbs- oder finanziellen Konsequenzen
an den Rangplatzierungen hängen.
