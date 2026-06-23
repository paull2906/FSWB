---
title: Daniel Silbermann
parent: Individual Contributions
nav_order: 1
---


# Daniel Silbermann

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,7

### Personal goals

Meine Persönlichen Ziele in diesem Modul sind zu lernen wie man Web-Aplicationen erstellt und verwaltet. Ich möchte mein Wissen im Fron-End und Back-End vertiefen und möchte allgemein verstehen wie Web-Aplicationen aufgebaut und unterhalten werden.

---

## Eidesstattliche Erklärung

**Daniel Silbermann 77208682221**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Login Fenster erstellt | Ich habe hier die Freiheit genossen selber entscheiden zu können was genau ich rein machen möchte und wie das fenster aussehen  soll. Vor alem Die möglichkeit Designtechnisch da freiheiten zu haben, hat mir sehr gefallen. Am Ende sieht es auch gut aus. | Die Challenge die ich überschritten habe war, dass der primary button nicht geklappt hat und ich diesen dann neu erstellen musste |
| 2 | Register Fenster erstellt | Auch hier hatte ich die Möglichkeit frei zu entscheiden. Zu erst hatte ich das Anmeldescreen erstellt. Worauf ich stolz bin ist, dass das Registrieren Fenster genau so aussieht wie das Anmeldefenster | Durch Mehr optionen bei der Registrierung ist die Karte länger geworden. Eine Challenge war es also, dass die Karte dennoch so central central aussieht wie beim Anmeldescreen. Das habe ich geschafft |
| 3 | Erstellung von der Forms.py | In der Vorlesung habe ich WTForms nicht ganz verstanden, fand es aber grundsätzlich interessant und auch für unser Projekt sinnhaft. Ich bin daher stolz darauf, dass ich es am Ende dennoch geschafft habe zu verstehen und sogar das Dokument zu erstellen. | Ich musste mir das komplett neu aneignen und verstehen was genau benötigt wird und wie ich an das Komme, was ich benötige. Am ende habe ich es verstanden |

## Design Decisions that I led



---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [Commit 1](https://github.com/hwrberlin/fswd/commit/d816e4), [Commit 2](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |  Gemini - Image Generation       |  Visuelle Umsetzung und Verfeinerung unserer eigenen UI-Konzeptvorstellung              |  https://github.com/paull2906/Musik-Quiz/blob/main/docs/01-value-propositions.md#target-scope                               |  In erster Linie hatten wir bereits visuelle skizzen und erste Ideen gezeichnet und waren grob mit dem design zufrieden. Um diese Visualisierung besser und verständlicher darzustellen, gaben wir Gemini die Aufgabe unser bisheriges UI realistischer und veranschaulicher darzustellen. Durch einen interativen Prozess und gezieltes Feedback, ergab sich dann schrittweise das gewünschte und fertige UI.                            |
| 02  |     Gemini (1)    |       Gefragt wie man einen gewissen Code erstellen kann         |              [forms.py](forms.py)                   |              Ich habe Gemini gefragt was man importieren muss für ein LogIn und Register Screen und auch nach dem Sinn gefragt um WTForms auch inhaltlich zu verstehen um das dann besser anzuwenden.             |   
| 3 |   Gemini(2)       |       Fragen weshalb die App nicht startet        |          [App.py](app.py)                      |          Ich habe Gemini die Fehlermeldung gezeigt und frage weshalb die App nicht startet                   |
| 4 | Gemini (3)         | Beim starten der App kam eine große Fehlermeldung, die ich nicht entziffern konnte. Ich habe diese also dann bei Gemini rein geschickt |  [App.py](app.py) | Die Fehlermeldung habe ich abgesenet und es ergabt sich, dass ich Kommata und andere formelles falsch geschickt habe 
| 5 | Gemini (4) | Generelle Fragen zum Code gestellt, wenn etwas nicht geklappt hat. | Überwiegend bei folgenden Codes: (templates/register-window.html) & (templates/login-window.html) | Generelle Fragen, wenn etwas nicht so geklappt hat wie ich es mir vorgestellt habe.
