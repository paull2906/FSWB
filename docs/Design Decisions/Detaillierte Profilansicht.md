---
title: template
parent: Design Decisions
---

{: .no_toc }
# Detaillierte Profilansicht

## Meta

Status
: Decided 

Updated
: 21-Jul-2026

## Problem Statement

Die Idee einer detaillierten Profilansicht (Spielhistorie, erstellte Quizze, ggf. Statistiken pro Nutzer) kam im Rahmen der Weiterentwicklung des Musik-Quiz auf. 
Das Datenmodell unterstützt das bereits, da User.scores und User.quizzes bereits als Relationships in db.py vorhanden sind. 
Eine Profilseite ließe sich rein technisch also ohne Schema-Änderung umsetzen, sondern nur über eine neue Route + Template.
Gleichzeitig besteht in der App bereits ein bekanntes, ungelöstes Datenschutzproblem: das öffentliche Leaderboard zeigt Username und
Wohnort jedes Spielers ohne Login-Schutz. Eine Profilseite würde diese Art der Datenexposition (Spielhistorie, ggf. weitere persönliche Felder) 
an einer zusätzlichen Stelle bündeln.

## Decision
Die detaillierte Profilansicht wird in dieser Projektphase nicht umgesetzt.
Begründung: Bevor eine Profilseite sinnvoll gebaut werden kann, muss zuerst geklärt werden, ob Profile öffentlich (für alle Spieler einsehbar) 
oder privat (nur für den jeweiligen Nutzer selbst) sein sollen. Diese Entscheidung hat direkte Auswirkungen auf Zugriffskontrolle und Datenmodell 
und ist keine reine UI-Erweiterung. Da das bestehende Leaderboard-Datenschutzproblem noch ungelöst ist, wäre es inkonsistent, dasselbe Muster mit 
einer Profilseite unreflektiert zu erweitern.
Zusätzlich steht der Implementierungsaufwand in keinem angemessenen Verhältnis zum Nutzen: Eine Profilansicht ist ein reines Zusatzfeature ("nice to have"), 
das nichts zur Kernfunktionalität der App (Quiz erstellen, spielen, sich auf dem Leaderboard vergleichen) beiträgt. 
Der scheinbar geringe technische Aufwand (Relationships sind bereits vorhanden) täuscht darüber hinweg, dass eine sauber durchdachte Umsetzung zusätzlich 
eine Datenschutz-Entscheidung und eine neue Zugriffskontroll-Prüfung. Diese Zeit ließe sich in der verbleibenden Projektlaufzeit
sinnvoller in Korrekturen mit höherem funktionalem Impact investieren.

Entschieden von: Leo Harnoth

## Regarded Options

Option A — Öffentliches Profil (für alle Spieler einsehbar)

Pro: höchster Gamification-Wert (Vergleich zwischen Spielern), technisch am einfachsten über die bestehenden Relationships umzusetzen.

Contra: erweitert das bestehende Datenschutzproblem des öffentlichen Leaderboards um zusätzliche personenbezogene Daten (Spielhistorie, erstellte Inhalte),
ohne dass eine Einwilligung dafür vorgesehen ist.

Option B — Privates Profil (nur für den eingeloggten Nutzer selbst sichtbar)

Pro: kein zusätzliches Datenschutzrisiko gegenüber Dritten, bietet trotzdem einen persönlichen Fortschrittsüberblick.

Contra: verliert genau den Vorteil, der die öffentliche Variante ursprünglich attraktiv gemacht hat (Vergleich zwischen Spielern).
Es bleibt nur eine persönliche Fortschrittsanzeige übrig, was den Nutzen zusätzlich schmälert.

Option C — Keine Profilansicht (gewählt)

Pro: kein zusätzliches Datenschutz- oder Scope-Risiko, hält den Fokus auf der Kernfunktion (Quiz erstellen/spielen), 
verschiebt die Entscheidung nicht auf eine unklare Zwischenlösung.

Pro: Aufwand steht nicht im Verhältnis zum Nutzen. Die Funktion ist rein ergänzend, während die Projektzeit für Korrekturen mit
größerer Wirkung benötigt wird.

Contra: verschenkt eine technisch günstige Gamification-Möglichkeit, die das Datenmodell bereits kostenlos hergeben würde.


