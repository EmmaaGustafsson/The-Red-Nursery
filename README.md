The Red Nursery

Textäventyr i Python för att öva **klasser, funktioner, loopar och moduler**. Skrivmaskinseffekt, blinkande “Press Enter”, enkel ASCII-figur som blir läskigare vid fel val, och JSON-loggning av rundor.

## Installation (Windows)
```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
-----------------------------
Uppdelning av projektet
# engine/game.py – Game-klassen (elev A):
  - Ilbron
# engine/ui.py – UI (typewriter + blink) (elev B):
  - Emmy
# engine/face.py – CreepyFace (elev C):
  - Emma
# data/story.py – Intro, scener, texter (elev C):
  - Emma
# util/storage.py – RunLogger (JSON-logg) (elev D):
  - Rasmus
# tests/test_game.py – PyTest (elev D):
  - Rasmus
