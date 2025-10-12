from dataclasses import dataclass
from typing import Dict, Any, Optional, List

@dataclass
class GameState:
    scene_id: str = ""
    is_running: bool = False

class Game:
    def __init__(self, story: Dict[str, Any], ui, logger=None):
        self.story = story
        self.ui = ui
        self.logger = logger or _NullLogger()
        self.state = GameState()

    def start(self, start_scene: Optional[str] = None):
        self.state.scene_id = start_scene or self.story["start"]
        self.state.is_running = True
        self.logger.log("game_start", scene=self.state.scene_id)
        while self.state.is_running:
            self._enter_scene(self.state.scene_id)

    def _enter_scene(self, scene_id: str):
        scene = self.story["scenes"][scene_id]
        self.logger.log("enter_scene", scene=scene_id)

        self.ui.typewriter(scene.get("text", ""))
        self.ui.write("")

        options: List[Dict[str, Any]] = scene.get("options") or []
        if scene.get("end", False) or not options:
            self.logger.log("game_end", scene=scene_id)
            self.state.is_running = False
            return

        self.ui.show_options(options)
        valid = [o["key"] for o in options]
        key = self.ui.get_input("Välj: ", valid)
        chosen = next(o for o in options if o["key"] == key)

        self.logger.log("choice", from_scene=scene_id, choice=key, goto=chosen["goto"])
        self.state.scene_id = chosen["goto"]

class _NullLogger:
    def log(self, *args, **kwargs):
        pass
