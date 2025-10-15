from dataclasses import dataclass  # enkel dataklass – vi slipper skriva egen __init__
import os
import json
# =========================
# Översikt (engine/game.py)
# - GameState: håller aktuell scen och om spelet kör
# - Game: kör loopen scen → val → nästa scen via UI
# =========================

@dataclass
class GameState:
    """Spelets nuvarande läge: vilken scen vi är i och om loopen ska rulla."""
    scene_id: str = ""      # id för aktuell scen
    is_running: bool = False  # True så länge huvudloopen ska köra

class Game:
    """Själva spelmotorn.
       Förväntar:
       - story: {"start": str, "scenes": {id: scen}}
       - ui: typewriter(text), write(text), show_options(options), get_input(prompt, valid_keys)
             valfritt: render_face(frame=0) för ASCII-art
       - logger: valfri, måste ha .log(event, **fields) om den skickas in
    """

    def __init__(self, story, ui, logger=None, face=None, right_cons=None, wrong_cons=None): ###La till stöd för ansiktsvisningen och konsekvenserna genom face, right_cons och wrong_cons
        # Spara beroenden och starta med tomt state
        self.story = story          # all berättelsedata (start + scenes)
        self.ui = ui                # användargränssnitt för utskrift och input
        self.face = face
        self.logger = logger or _NullLogger()  # tyst logger om ingen skickas in
        self.state = GameState()    # scene_id="" och is_running=False från början
        self.right_cons = right_cons or []
        self.wrong_cons = wrong_cons or []
        self.wrong_count = 0 ###La till wrong_count 0 och self.correct_count 0 , så programmet vet vilket ansikte den skall börja med vid första fel svar. Detta kopplas till json.
        self.correct_count = 0

    def start(self, start_scene=None):
        """Väljer startscen och kör huvudloopen tills spelet tar slut."""
        self.state.scene_id = start_scene or self.story["start"]  # starta på given eller definierad start-scen
        self.state.is_running = True                               # tänd loopen
        self.logger.log("game_start", scene=self.state.scene_id)   # logga att spelet startar

        # Huvudloop: processa scener tills en slut-scen stoppar spelet
        while self.state.is_running:
            self._enter_scene(self.state.scene_id)

    def _enter_scene(self, scene_id):
        """Rendera en scen, hantera spelarens val och bestäm nästa scen.
           Avslutar spelet om scenen saknas eller är märkt som slut.
        """
        scenes = self.story.get("scenes", {})  # hämta alla scener

        # Skydd: om scen-id saknas i story → informera, logga och stoppa snyggt
        if scene_id not in scenes:
            self.ui.typewriter(f"Saknar scen: {scene_id}")
            self.state.is_running = False
            self.logger.log("game_end", scene=scene_id, reason="missing_scene")
            return

        scene = scenes[scene_id]                       # slå upp scenobjektet
        self.logger.log("enter_scene", scene=scene_id) # logga inträde i scenen
        

        # Berättelsetext
        self.ui.typewriter(scene.get("text", ""))
        self.ui.write("")

        # Slutscen eller val
        options = scene.get("options") or []
        if scene.get("end", False) or not options:
            self.logger.log("game_end", scene=scene_id)  # logga att spelet tar slut här
            self.state.is_running = False                # stäng av loopen
            self.save_results("won") ###visar won i results.json
            return

        import random

        self.ui.show_options(options)
        valid_keys = [o["key"] for o in options]
        choice_key = self.ui.get_input("Choose: ", valid_keys) ###Byter ut ordet "Välj:" till "Choose:" då spelet är på engelska
        chosen = next(o for o in options if o["key"] == choice_key)

        # Slumpa om svaret blir rätt eller fel (50/50)
        if random.choice([True, False]):
            self.correct_count += 1 ### Denna ökar vid rätt svar, kopplas till json så vi får korrekta utfall
            self.ui.type_line(random.choice(self.right_cons))
        else:
            self.wrong_count += 1 ### denna ökar vid fel svar, kopplas till json så vi får korrekta utfall
            self.ui.type_line(random.choice(self.wrong_cons))
        # visa ansikte
        if self.face: 
            self.face.show(self.wrong_count)
        if self.wrong_count >= len(self.face.CREEPY_FACE) - 1: ###La till detta så spelet visar att vi förlorat när hela ansiktet visas annars fortsätter spelet tills vi klarar det även fast man har hela ansiktet.
            self.ui.typewriter("\nYOU HAVE BEEN TRAPPED IN THE RED NURSERY.") ###Meddelar detta när vi förlorar
            self.ui.typewriter("YOU DIED.") ###Meddelar detta när vi förlorar
            self.state.is_running = False
            self.logger.log("game_end", scene=scene_id, reason="too_many_wrongs")
            self.save_results("lost")###visar lost i results.json
            return ###Avslutar vid förlust
        self.logger.log("choice", from_scene=scene_id, choice=choice_key, goto=chosen["goto"])
        self.state.scene_id = chosen["goto"]
    def save_results(self, result): ### Detta sparar resultaten till en JSON
        data = {
        "correct_answers": self.correct_count,
        "wrong_answers": self.wrong_count,
        "result": result
    }
        with open("results.json", "w") as f: ###skapar en results.json
         json.dump(data, f, indent=4)

class _NullLogger:
    """Tyst logger: tar emot alla logganrop men gör ingenting."""
    def log(self, *args, **kwargs):
        pass
