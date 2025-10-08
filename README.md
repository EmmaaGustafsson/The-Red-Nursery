# Haunted House – The Red Nursery (Text Adventure)

Ett nybörjarvänligt textäventyr i Python för att öva **klasser, funktioner, loopar och moduler**. Spelet använder skrivmaskinseffekt, blinkande “Press Enter”, en enkel ASCII-figur som blir läskigare vid fel val, samt JSON-loggning av rundor.

## Installation
```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


A 2-choice text adventure:
- Typewriter effect for all text
- Beginner-friendly code (few helpers, lots of comments)
- A simple "creepy face" that reveals more after wrong choices
- Clear feedback line: 'You chose to ..., Now ...'
- Random correct option per scene (0 or 1)
- Pulsing '>> Press Enter <<' and ('GAME OVER' / 'YOU SURVIVED') msvcrt (Windows)