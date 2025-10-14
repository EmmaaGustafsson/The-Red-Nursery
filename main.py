from engine.face import CreepyFace
from engine.game import GameState, Game
from engine.ui import UI
from data.story import INTRO, SCENES, WIN_TEXT, LOSE_TEXT, RIGHT_CONSEQUENCES, WRONG_CONSEQUENCES

try:
    from colorama import init as colorama_init, Style
    colorama_init(autoreset=True)
    TITLE_DECOR = Style.BRIGHT
except Exception:
    TITLE_DECOR = ""

# ---- NYTT: gör om SCENES (list) till motorformatet (dict med id -> scen) ----
def build_story_from_list(scenes_list, win_lines):
    scenes = {}
    for i, s in enumerate(scenes_list):
        scene_id = "intro" if i == 0 else f"s{i}"
        text = s.get("prompt", "")
        opts = s.get("options", [])
        next_id = f"s{i+1}" if i + 1 < len(scenes_list) else "end"
        options = []
        # om options är t.ex. ('val1','val2')
        for idx, label in enumerate(list(opts), start=1):
            options.append({"key": str(idx), "label": str(label), "goto": next_id})
        scenes[scene_id] = {"text": text, "options": options}
    # lägg en tydlig slut-scen som visar WIN_TEXT
    scenes["end"] = {"text": "\n".join(win_lines), "end": True}
    return {"start": "intro", "scenes": scenes}

def main():
    TYPE_DELAY = 0.075
    PULSE_ON_MS  = 500
    PULSE_OFF_MS = 450

    ui = UI(type_delay=TYPE_DELAY, pulse_on_ms=PULSE_ON_MS, pulse_off_ms=PULSE_OFF_MS)
    face = CreepyFace()

    # ---- NYTT: UI-adapter så motorn får metoderna den förväntar sig ----
    if not hasattr(ui, "typewriter"):
        ui.typewriter = ui.type_line  # alias
    if not hasattr(ui, "write"):
        def _write(text):
            print() if text == "" else print(text)
        ui.write = _write
    if not hasattr(ui, "show_options"):
        def _show_options(options):
            for o in options:
                print(f"{o.get('key')}) {o.get('label')}")
        ui.show_options = _show_options
    if not hasattr(ui, "get_input"):
        def _get_input(prompt, valid_keys):
            while True:
                ans = input(prompt).strip()
                if not valid_keys or ans in valid_keys:
                    return ans
                print("Välj: " + " / ".join(valid_keys))
        ui.get_input = _get_input

    # Titel + intro
    ui.type_line(f"{TITLE_DECOR}HAUNTED HOUSE: The Red Nursery", delay=0.1)
    ui.type_lines(INTRO, delay=TYPE_DELAY)
    ui.pulse_until_enter(">> Press Enter to begin <<")
    ui.print_blank()

    # ---- NYTT: bygg story i rätt format åt motorn ----
    story = build_story_from_list(SCENES, WIN_TEXT)

    game = Game(
        story=story,
        ui=ui,
        # ingen autosave/resume i motorn längre
    )

    # ---- ÄNDRAT: start returnerar inget, motorn visar sluttext i "end"-scenen ----
    game.start()

    ui.print_blank()
    ui.pulse_until_enter("Tryck Enter för att avsluta")

if __name__ == "__main__":
    main()
