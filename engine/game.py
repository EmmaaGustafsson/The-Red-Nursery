from dataclasses import dataclass  # importerar hjälp för enkel dataklass

@dataclass  # genererar __init__/__repr__/__eq__ automatiskt
class GameState:  # håller spelets nuvarande läge
    scene_id: str = ""  # id för aktuell scen
    is_running: bool = False  # om huvudloopen ska fortsätta

class Game:  # själva spelmotorn
    def __init__(self, story, ui, logger=None):  # sätter upp motorn med data, UI och valfri logger
        self.story = story  # hela berättelsen (start + scenes)
        self.ui = ui  # gränssnitt för utskrift/inmatning
        self.logger = logger or _NullLogger()  # använd given logger eller en tyst standard
        self.state = GameState()  # starta med tomt speltillstånd

    def start(self, start_scene=None):  # startar spelet från given scen eller standard
        self.state.scene_id = start_scene or self.story["start"]  # välj startscen
        self.state.is_running = True  # slå på huvudloopen
        self.logger.log("game_start", scene=self.state.scene_id)  # logga att spelet börjar
        while self.state.is_running:  # kör så länge spelet är aktivt
            self._enter_scene(self.state.scene_id)  # processa aktuell scen

    def _enter_scene(self, scene_id):  # spelar upp en scen och bestämmer nästa
        scenes = self.story.get("scenes", {})  # hämta alla scener
        if scene_id not in scenes:  # om scenen saknas
            self.ui.typewriter(f"Saknar scen: {scene_id}")  # meddela spelaren
            self.state.is_running = False  # stoppa spelet
            self.logger.log("game_end", scene=scene_id, reason="missing_scene")  # logga orsak
            return  # avsluta scenhanteringen

        scene = scenes[scene_id]  # hämta scenobjektet
        self.logger.log("enter_scene", scene=scene_id)  # logga att vi gick in i scenen

        if scene.get("art") == "creepy_face" and hasattr(self.ui, "render_face"):  # specialfall för ASCII-art
            art = self.ui.render_face(frame=0)  # rendera första ramen
            if art:  # om något genererades
                self.ui.write(art)  # skriv ut grafiken
                self.ui.write("")  # tom rad för luft

        self.ui.typewriter(scene.get("text", ""))  # skriv scenens berättelsetext
        self.ui.write("")  # tom rad efter text

        options = scene.get("options") or []  # hämta valen eller tom lista
        if scene.get("end", False) or not options:  # om scenen är slut eller saknar val
            self.logger.log("game_end", scene=scene_id)  # logga att spelet tar slut här
            self.state.is_running = False  # stäng av loopen
            return  # avsluta scenen

        self.ui.show_options(options)  # visa valen för spelaren
        valid_keys = [o["key"] for o in options]  # lista med tillåtna knappval
        choice_key = self.ui.get_input("Välj: ", valid_keys)  # läs ett giltigt val från användaren
        chosen = next(o for o in options if o["key"] == choice_key)  # hitta valt alternativ

        self.logger.log("choice", from_scene=scene_id, choice=choice_key, goto=chosen["goto"])  # logga valet
        self.state.scene_id = chosen["goto"]  # hoppa till nästa scen

class _NullLogger:  # logger som inte gör något (säker standard)
    def log(self, *args, **kwargs):  # accepterar vilka argument som helst
        pass  # inga sidoeffekter
