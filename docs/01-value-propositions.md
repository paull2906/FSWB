---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## The Problem

Der Markt für Quize ist groß, aber falsch zugeschnitten. Das führt zu einem Problem bzw. einer Situation bei der sich beide Seiten der Plattform nicht komplett fühlen.
  - # Problem A - Für Quizmaster
    - Wer heute ein anspruchsvolles Musik-Quiz zu einem Nischen-Genre erstellen möchte, steht heute vor einer Sackgasse: Google Forms oder Kahoot bieten keine Audio-Integration. Youtube-Quizze in Discord-Servern oder persönlich sind manuell, nicht skalierbar und folglich auch nicht wirklich messbar.
      Das Ergebnis: Das Wissen des des Experten bleibt im Kopf, weil keine Plattform existiert, durch die er sein Wissen teilen kann bzw. sich beweisen kann.

  - # Problen B - Für Spieler
    - Anbieter wie Heardle, Youtube oder auch Spotify-interne Features fokussieren auch Songs, die in dem Moment oder vor kurzen sehr angesagt waren. Für jemanden, der sich 5 Jahre lang mit der Geschichte hinter den Songs auseinaner gesetzt hat, ist das dann quasi nicht wirklich betreffend und ansprechend.
      Darüber hinaus fehlt jede Form von persistentem Wettbewerb also ein langfristiger Wettbewerb, der nicht direkt nach dem Duell verschwindet. Und genau dadurch entsteht das Problem: Durch den fehlenden persistenten Wettbewerb entsteht kein Ehrgeiz sich langfristig zu duellieren und sich zu messen. Kein Leaderboard, kein Vergleich mit der lokalen Community, kein Link, den man in einem Chat teilen kann, der dann bedeutung hat.
  - # Verbindende Marklücke
    - Es existiert keine Plattform, die das Erstellen und den Konsum von Musik-Quizen im Nischen-Segment oder auch im Allseits bekannten Genre gut vereint - mit echter Spotify-Audio-Integration, Unser-Generated Content und einem Ranglisten-System, das über eine Spielrunde hinaus gespeichert wird und dadurch danna auch an Bedeutung gewinnt. LionsRecords schließt exakt diese Lücke.
      
## Our Solution

LionRecords ist eine Web-Aplication, auf der Quizmaster eigene Audio-Quizze erstellen und Player diese Kompetitiv lösen können. Mit persistenten Ranglisgen Weltweil werden kompetitive Spieler gehalten, da sie den Drang haben sich und anderen etwas zu beweisen und durch gute Positionierung gut darzustehen.

- Spotify API: 30s Audio Snippets
- User-Generated Quiz-Pakete
- Echtzeit-Scoring mit bewertung nach verschiedenen Kategorien
- Geo-Leaderboards (Local oder auch Global)
- Share-Link per Quiz-Ergebnis
- Genre-Ranking für Creator
- Responsive Web App

## Target User(s)

LionRecords visiert eine sehr spezifische, aber auch weltweit relevante Gruppe an: 
  - ## Menschen, für die Musik kein Hobby ist, sondern eine Identität
Sie kennen nicht nut den Hit - sie kennen auch die vertrendenden Musiker, die Texte, die Geschichte dahinter und vieles Mehr.
LionRecords möchte nicht nur eine "Musikquiz-App" sein, sondern diesen Personen eine Bühne bieten, um sich auszutauschen aber auch um sich zu duellieren. 
  - Konkrete Beispiele könnte der Berliner sein, der jeden deutschen Rap-Release seit 1997 auswendig kennt, die Wienerin, die im Jazz-Forum moderiert oder auch der Discord-Server mit tauseden Mitgliedern, in dem "Underrated-Hits" oder allgemein Musik geteilt wird, die einen gerade interessiert. 

##  Happy Path

### Happy Path A: Der Quizmaster
# Ziel: Erstellung eines Nischen-Musik-Quizzes zur Steigerung der eigenen Sichtbarkeit.
- Einstiegspunkt: Der Creator sieht, dass sein spezifisches Nischen-Genre noch unbesetzt ist (First-Moves-Anreiz)
- Schritt 1: Klick auf "Create" und Anmeldung bei Spotify OAuth
- Schritt 2: Nutzung der Spotify-Suchmaske. Creator fügt bis zu 15 Songs hinzu, benennt das Quiz, wählt das Genre und legt Schwierigkeitsgrad fest
- Schritt 3: Testen ob alles so klappt wie er Möchte. Creator kann hier einstellen, dass die Ausschnitte 30s lang sind und es dann veröffentlichen.
- Abschluss: Das Quiz ist live und für alle sichtbar. Der Creator sgteigt sofort auf den Platz 1 des Leaderboards und das Ergebnis wird gespeichert. Es entsteht nun den Anreiz den Creator besiegen zu wollen.

### Happy Path B: Der Player
# Ziel: Absolvieren eines Quizzes und Platzierung in der Community.
- Der Spieler stöbert vorerst durch die Vorhandenen kategorien, kann diese gegebenenfalls auch filtern und wählt dann ein Quiz aus, um sich zu challengen.
- Schritt 1: Klickt auf "Play" und meldet sich bei Spotify OAuth an, um den Punktestand dauerhaft zu speichern.
- Schritt 2: Das Spiel läuft. Der Spieler hört nun 30s-Snippets, ein Punktesystem erlaubt es dem Spieler Punkte durch verschiedene richtige Angaben zu erhalten.
- Schritt 3: Am Ende erscheint ein Gesamtscore und die Platzierung im Vergleich mit anderen Spielern. Durch einen geografischen Filter (z.B. "Berlin") könnte er einen lokalen Rang einsehen
- Abschluss: Der Spieler kann jetzt sein Ergebnis und seine Platzierung durch einen Link in einem Discord Server teilen, wodruch ein kompetitiver Kreislauf mit Freunden und der Comunity entsteht.

---

## Target Scope

[Include your visual scoping of the web app (e.g., UI screens scribbles), as elaborated at start of the project as part of your Assignment.]
