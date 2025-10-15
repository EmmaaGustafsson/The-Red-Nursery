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


### Lagt in "save_game" + "load_game" in i util.storage och skrev kommentarer vad koderna gör. Jag testade även ifall funktionen fungerade genom att skapa test_storage.py fil. 100% passed. Skrev in lite random data exempelvis "health: 100" och "location: forest" och såg ifall load_game kunde ta info från det vi "saveat" genom detta "assert loaded_data == test_data". Fick error i början när jag försökte köra pytest från root i projektet och även efter det men löste det genom att skapa en pytest.ini fil, måste läsa mer om vad exakt det är för något. - Rasmus


### Vi hade problem med att spelet fungerade men ej visade upp något ansikte, detta löstes genom att lägga till face=face i game samt right/wrong_cons för att få ansiktet vid rätt tillfälle. Vi la även till stöd i game.py i __init__ till face och right/wrong_cons. Detta löste ansiktsproblemet men då uppstod nästa problem, spelet fortsatte ända fram tills att vi klarade det även fast det ska avslutas när ansiktet nått maxgränsen (vi kunde inte förlora). Detta löstes genom att lägga in en if-sats under game.py-_enter_scene där ifall vi når maxgränsen på wrong_count så får vi LOSE_TEXT från data-story.py. Inom samma if-sats las in return så spelet avslutas och man får börja om.
### Snabb fix med att när man skulle välja alternativ 1 eller 2 så stod det "Välj:" men eftersom spelet är på engelska ändrades detta till "Choose:"
### La till en json som heter results.json som visar antal rätt och fel svar samt ifall man vann eller inte. Dessa rader som kopplas till json finns kommenterade i game.py