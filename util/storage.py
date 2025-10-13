<<<<<<< HEAD
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
=======
# ELEV D

import json
from datetime import datetime
from pathlib import Path

class RunLogger:
    """Append simple run results to a JSON file."""
    def __init__(self, path: str):
        self.path = Path(path)

    def log_result(self, result: str, wrong: int, total_scenes: int):
        entry = {
            "ts": datetime.now().isoformat(timespec="seconds"),
            "result": result,
            "wrong": wrong,
            "total": total_scenes,
        }
        data = []
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
        data.append(entry)
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
>>>>>>> nursery-b
