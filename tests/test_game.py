# ELEV D

from engine.face import CreepyFace
from engine.game import Game
from util.storage import RunLogger

def test_face_bounds():
    f = CreepyFace()
    f.show(-5)  # should not crash
    f.show(99)  # should not crash

def test_runlogger(tmp_path):
    p = tmp_path / "run_log.json"
    logger = RunLogger(str(p))
    logger.log_result("win", wrong=1, total_scenes=6)
    assert p.exists()
    assert '"result": "win"' in p.read_text(encoding="utf-8")

def test_game_win_and_lose_without_input():
    class FakeUI:
        def type_line(self, *a, **k): pass
        def type_lines(self, *a, **k): pass
        def pulse_until_enter(self, *a, **k): pass
        def print_blank(self): pass
        def ask_choice(self, *a, **k): return 0  # always pick left option

    scenes = [
        {"prompt":"p1","options":("a","b")},
        {"prompt":"p2","options":("a","b")},
    ]
    face = CreepyFace()
    ui = FakeUI()

    g1 = Game(scenes, ui, face, right_cons=["ok"], wrong_cons=["bad"], max_wrong=1, correct_map=[0,0])
    assert g1.play() == "win"

    g2 = Game(scenes, ui, face, right_cons=["ok"], wrong_cons=["bad"], max_wrong=1, correct_map=[1,1])
    assert g2.play() == "lose"