<<<<<<< HEAD
The Red Nursery

Textäventyr i Python för att öva **klasser, funktioner, loopar och moduler**. Skrivmaskinseffekt, blinkande “Press Enter”, enkel ASCII-figur som blir läskigare vid fel val, och JSON-loggning av rundor.

## Installation (Windows)
=======
# Haunted House – The Red Nursery (Text Adventure)

Ett nybörjarvänligt textäventyr i Python för att öva **klasser, funktioner, loopar och moduler**. Spelet använder skrivmaskinseffekt, blinkande “Press Enter”, en enkel ASCII-figur som blir läskigare vid fel val, samt JSON-loggning av rundor.

## Installation
>>>>>>> nursery-b
```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
<<<<<<< HEAD
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


### Lagt in "save_game" + "load_game" in i util.storage och skrev kommentarer vad koderna gör. Jag testade även ifall funktionen fungerade genom att skapa test_storage.py fil. 100% passed. Skrev in lite random data exempelvis "health: 100" och "location: forest" och såg ifall load_game kunde ta info från det vi "saveat" genom detta "assert loaded_data == test_data". Fick error i början när jag försökte köra pytest från root i projektet och även efter det men löste det genom att skapa en pytest.ini fil, måste läsa mer om vad exakt det är för något. - Rasmus
=======


A 2-choice text adventure:
- Typewriter effect for all text
- Beginner-friendly code (few helpers, lots of comments)
- A simple "creepy face" that reveals more after wrong choices
- Clear feedback line: 'You chose to ..., Now ...'
- Random correct option per scene (0 or 1)
- Pulsing '>> Press Enter <<' and ('GAME OVER' / 'YOU SURVIVED') msvcrt (Windows)
>>>>>>> nursery-b
