from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from pathlib import Path
import json

@dataclass
class GameState:
    scene_id: str = ""
    is_running: bool = False

class Game:
    """
    Minimal motor med save/load. Passar UI (write/typewriter/show_options/get_input),
    Face via ui.render_face(), och STORY-formatet {"start": str, "scenes": {id: scene}}.
    """
    def __init__(self, story: Dict[str, Any], ui, logger=None,
                 save_path: Optional[Path] = None, autosave: bool = False):
        self.story = story
        self.ui = ui
        self.logger = logger or _NullLogger()
        self.state = GameState()
        self.save_path = Path(save_path) if save_path else None
        self.autosave = bool(autosave)

    def start(self, start_scene: Optional[str] = None, resume: bool = False):
        if resume and self.load_state():
            self.state.is_running = True
            self.logger.log("resume", scene=self.state.scene_id)
        else:
            self.state.scene_id = start_scene or self.story["start"]
            self.state.is_running = True
            self.logger.log("game_start", scene=self.state.scene_id)
        while self.state.is_running:
            self._enter_scene(self.state.scene_id)

    def _enter_scene(self, scene_id: str):
        scenes = self.story.get("scenes", {})
        if scene_id not in scenes:
            self.ui.typewriter(f"Saknar scen: {scene_id}")
            self.state.is_running = False
            self.logger.log("game_end", scene=scene_id, reason="missing_scene")
            if self.autosave:
                self.save_state()
            return

        scene = scenes[scene_id]
        self.logger.log("enter_scene", scene=scene_id)

        if self.autosave:
            self.save_state()  # spara vid scenstart så resume funkar även vid avbrott

        if scene.get("art") == "creepy_face" and hasattr(self.ui, "render_face"):
            art = self.ui.render_face(frame=0)
            if art:
                self.ui.write(art)
                self.ui.write("")

        self.ui.typewriter(scene.get("text", ""))
        self.ui.write("")

        options: List[Dict[str, Any]] = scene.get("options") or []
        if scene.get("end", False) or not options:
            self.logger.log("game_end", scene=scene_id)
            self.state.is_running = False
            if self.autosave:
                self.save_state()
            return

        self.ui.show_options(options)
        valid_keys = [o["key"] for o in options]
        choice_key = self.ui.get_input("Välj: ", valid_keys)
        chosen = next(o for o in options if o["key"] == choice_key)

        self.logger.log("choice", from_scene=scene_id, choice=choice_key, goto=chosen["goto"])
        self.state.scene_id = chosen["goto"]
        if self.autosave:
            self.save_state()

    # -------- save/load --------
    def save_state(self):
        if not self.save_path:
            return
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"scene_id": self.state.scene_id, "is_running": self.state.is_running}
        self.save_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        self.logger.log("save_state", path=str(self.save_path))

    def load_state(self) -> bool:
        if not self.save_path or not self.save_path.exists():
            return False
        try:
            data = json.loads(self.save_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return False
        self.state.scene_id = str(data.get("scene_id") or self.story["start"])
        self.state.is_running = bool(data.get("is_running", False))
        self.logger.log("load_state", path=str(self.save_path), scene=self.state.scene_id)
        return True

class _NullLogger:
    def log(self, *args, **kwargs):
        pass
