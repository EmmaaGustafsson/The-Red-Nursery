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

def main():
    # ===== Your settings preserved =====
    TYPE_DELAY = 0.075      # seconds per character
    MAX_WRONG  = 3          # mistakes before game over
    PULSE_ON_MS  = 500      # visible time
    PULSE_OFF_MS = 450      # hidden time

    ui = UI(type_delay=TYPE_DELAY, pulse_on_ms=PULSE_ON_MS, pulse_off_ms=PULSE_OFF_MS)
    face = CreepyFace()

    # Title + intro (same feel as your script)
    ui.type_line(f"{TITLE_DECOR}HAUNTED HOUSE: The Red Nursery", delay=0.1)
    ui.type_lines(INTRO, delay=TYPE_DELAY)
    ui.pulse_until_enter(">> Press Enter to begin <<")
    ui.print_blank()

    game = Game(
        ui=ui,
        scenes: Dict[str, Dict[str, Any]] = {}
        # correct_map randomized internally (0/1 per scene), exactly like your code
    )

    result = game.play()  # 'win' or 'lose'

    ui.print_blank()
    if result == "win":
        ui.type_lines(WIN_TEXT, delay=TYPE_DELAY)
        ui.pulse_until_enter("YOU SURVIVED")
    else:
        ui.type_lines(LOSE_TEXT, delay=TYPE_DELAY)
        ui.pulse_until_enter("YOU DIED")

    # Log run for the project requirement
    logger.log_result(result=result, wrong=game.wrong, total_scenes=len(SCENES))

if __name__ == "__main__":
    main()