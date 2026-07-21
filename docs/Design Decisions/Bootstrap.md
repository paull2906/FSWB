---
title: 00 Bootstrap als CSS-Framework
parent: Design Decisions
---
{: .no_toc }
# Bootstrap als CSS-Framework

## Meta
Status
: **Decided**

Updated
: 21-Jul-2026

## Problem Statement
Wir brauchten ein vernünftiges Fundament für das Styling unserer Anwendung. Von Anfang alles mit CSS zu machen, hätte ewig gedauert und am Ende wäre es wahrscheinlich trotzdem nicht besonders einheitlich oder schön geworden. Uns fehlte auch einfach die Zeit, jede Komponente (Buttons, Formulare, Navigationsleisten, Grids und so weiter) komplett selbst zu entwickeln und dabei noch responsives Verhalten im Blick zu behalten. Wir wollten etwas, das schnell einsatzbereit ist und dazu noch gut aussieht.

## Decision
Wir haben uns dazu entschieden, Bootstrap als Basis für unser Styling zu verwenden. Der Ausschlag dafür war eigentlich relativ schnell klar: Es spart uns extrem viel Zeit, weil man nicht bei null anfangen muss, sondern auf ein riesiges Set an fertigen, getesteten Komponenten zurückgreifen kann. Die Einbindung war unkompliziert und man hat quasi sofort ein Ergebnis gesehen, das schon ordentlich aussieht, ohne dass man selbst extremen Aufwand betreiben musste wie bei reinem CSS zum Beispiel.

Den letzten Ausschlag hat dann ein Bootswatch-Theme gegeben, das uns optisch einfach überzeugt hat. Dadurch bekommt man mit ein paar Zeilen ein durchgängiges, modernes Design, ohne dass man selbst großen Aufwand betreiben muss. Weil der Aufwand so gering und der Nutzen im Verhältnis dazu so groß war, ist die Entscheidung ziemlich schnell gefallen.

Zusätzlich zu Bootstrap nutzen wir noch eigenes CSS, allerdings eher ergänzend für kleinere individuelle Anpassungen, die über das hinausgehen, was Bootstrap standardmäßig anbietet.

## Regarded Options

| Option | Vorteile | Nachteile |
|---|---|---|
| **Bootstrap + Bootswatch-Theme** (gewählt) | Sehr schnell startklar, riesige Auswahl an fertigen Komponenten, sieht durch das Theme direkt gut und stimmig aus, einfach einzubinden, gute Community/Dokumentation | Man ist ein Stück weit an die Bootstrap-typische Optik gebunden, wenn man nicht zusätzlich anpasst; eigene CSS-Overrides können mit Bootstrap-Klassen kollidieren |
| **Reines, selbst geschriebenes CSS** | Volle Kontrolle über jedes Detail, kein "Bootstrap-Look" | Extrem zeitaufwendig, hohes Risiko für Inkonsistenzen, responsives Verhalten muss komplett selbst gebaut und getestet werden |

Am Ende war die Kombination aus Zeitersparnis, einfacher Umsetzung und dem optischen Ergebnis durch das Bootswatch-Theme einfach das überzeugendste Gesamtpaket.
