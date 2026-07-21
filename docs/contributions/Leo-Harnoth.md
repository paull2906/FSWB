---
title: Leo Harnoth
parent: Individual Contributions
nav_order: 1
---


# Leo Harnoth 

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade
1,3

### Personal goals

Modellierungen technisch umsetzen; umfangreiche Ergebnisdokumentation

---

## Eidesstattliche Erklärung

**Leo Harnoth, Matrikelnr.: 77208244796**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | app.py aufgebaut | Ich bin stolz, das gesamte Backend-Grundgerüst der App entworfen und implementiert zu haben. Dabei konnte ich lernen, wie Routing, Session-Handling und Datenbank-Anbindung in Flask sauber zusammenspielen. | Die wohl größte Herausforderung war, dass ich Großteile des Codes fast vollständig offline schreiben musste und dadurch keinen Live-Zugriff auf Kursinhalte oder YouTube-Tutorials hatte. Ich musste daher mit vorab angefertigten Screenshots und bereits angeeignetem Wissen arbeiten und vieles aus dem Gedächtnis rekonstruieren. |
| 2 | itunes.py aufgebaut | Ich konnte die Musikquelle der App über die öffentliche iTunes Search API aufbauen, ganz ohne API-Key, Authentifizierung oder Kosten. | Eine Herausforderung war die Cover-Auflösung: Die API gibt standardmäßig nur ein 100×100-Bild zurück. Die Lösung, die URL per String-Replace von 100x100 auf 300x300 umzuschreiben, ist nicht dokumentiert und musste ich durch Ausprobieren herausfinden. |
| 3 | Design Decision: Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1 geleitet | Ich bin stolz, eine produktstrategische Entscheidung argumentativ fundiert hergeleitet zu haben, welche direkten Einfluss auf die Architektur hat (kein Billing, alle Kernfeatures offen). | Die Herausforderung war, drei konkrete Monetarisierungsoptionen gegeneinander abzuwägen und sauber zu begründen, warum eine Paywall das Cold-Start-Problem nur verschärft, statt es zu lösen. |

## Design Decisions that I led

1. Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1
2. Detaillierte Profilansicht
3. Anti-Cheat-Mechanismus für Scores


---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| app.py | [app.py](https://github.com/paull2906/Musik-Quiz/blob/main/app.py) | [HWR Berlin: FSWD](https://hwrberlin.github.io/fswd/git.html), [Python-Doku](https://docs.python.org/3/library/difflib.html), [Youtube Tutorial about SQLAlchemy](https://youtu.be/jobpptS9f8I?si=2ZG-9xSyMyq2lfS6) |
| itunes.py | [itunes.py](https://github.com/paull2906/Musik-Quiz/blob/main/itunes.py) | [iTunes Search API](https://performance-partners.apple.com/search-api), [Python-Doku urllib](https://docs.python.org/3/library/urllib.request.html) |
| Design Decision: Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1 | [Design Decision: Kostenloser Zugang zu LiveRecords - keine Paywall in Phase 1.md](https://github.com/paull2906/Musik-Quiz/blob/main/docs/Design%20Decisions/Kostenloser%20Zugang%20zu%20LiveRecords%20-%20keine%20Paywall%20in%20Phase%201.md) | Diskussionen in der Gruppe nach der Peer Review |
| Design Decision: Detaillierte Profilansicht | [Design Decision: Detaillierte Profilansicht](https://github.com/paull2906/Musik-Quiz/blob/main/docs/Design%20Decisions/Detaillierte%20Profilansicht.md) | Diskussionen in der Gruppe nach dem Oral Exam |
| Design Decision: Anti-Cheat-Mechanismus für Scores | [Design Decision: Anti-Cheat-Mechanismus für Scores](https://github.com/paull2906/Musik-Quiz/blob/main/docs/Design%20Decisions/Anti-Cheat-Mechanismus%20für%20Scores.md) | Diskussionen in der Gruppe nach dem Oral Exam |
---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Claude (1) | Fehlerbehebung bei app.py | [app.py](https://github.com/paull2906/Musik-Quiz/blob/main/app.py) | Ich habe claude.ai die Fehlermeldungen gegeben und mir von der KI dann Vorschläge zur Behebung geben lassen |
| 02  | Claude (2) | Fehlerbehebung bei itunes.py | [itunes.py](https://github.com/paull2906/Musik-Quiz/blob/main/itunes.py) | Ich habe claude.ai die Fehlermeldungen gegeben und mir von der KI dann Vorschläge zur Behebung geben lassen |


