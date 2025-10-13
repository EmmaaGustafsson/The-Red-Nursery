import json

def save_game(data, filename="savegame.json"): # skapar "save_game", möjlighet att spara spel i filen "savegame.json"
    with open(filename, "w") as f:
        json.dump(data, f)

def load_game(filename="savegame.json"): # Laddar åter upp spelet igen där vi sparat spelet genom att gå in i filen "savegame.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
