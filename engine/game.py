from dataclasses import dataclass  # enkel dataklass – vi slipper skriva egen __init__

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

    def __init__(self, story, ui, logger=None):
        # Spara beroenden och starta med tomt state
        self.story = story          # all berättelsedata (start + scenes)
        self.ui = ui                # användargränssnitt för utskrift och input
        self.logger = logger or _NullLogger()  # tyst logger om ingen skickas in
        self.state = GameState()    # scene_id="" och is_running=False från början

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

        # Valfri ASCII-art: visas bara om scenen ber om det och UI kan rendera
        if scene.get("art") == "creepy_face" and hasattr(self.ui, "render_face"):
            art = self.ui.render_face(frame=0)
            if art:
                self.ui.write(art)
                self.ui.write("")

        # Berättelsetext
        self.ui.typewriter(scene.get("text", ""))
        self.ui.write("")

        # Slutscen eller val
        options = scene.get("options") or []
        if scene.get("end", False) or not options:
            self.logger.log("game_end", scene=scene_id)  # logga att spelet tar slut här
            self.state.is_running = False                # stäng av loopen
            return

        # Visa val, läs ett giltigt val och hoppa
        self.ui.show_options(options)                          # rendera alternativen
        valid_keys = [o["key"] for o in options]               # tillåtna val-tangenter
        choice_key = self.ui.get_input("Välj: ", valid_keys)   # läs användarens val
        chosen = next(o for o in options if o["key"] == choice_key)  # hitta valt alternativ

        # Logga valet och byt scen
        self.logger.log("choice", from_scene=scene_id, choice=choice_key, goto=chosen["goto"])
        self.state.scene_id = chosen["goto"]  # nästa scen körs i nästa loop-varv

class _NullLogger:
    """Tyst logger: tar emot alla logganrop men gör ingenting."""
    def log(self, *args, **kwargs):
        pass
