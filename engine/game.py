# ELEV A

import random

class Game:
    def __init__(self, scenes, ui, face, right_cons, wrong_cons, max_wrong=3, correct_map=None):
        self.scenes = scenes
        self.ui = ui
        self.face = face
        self.right_cons = right_cons
        self.wrong_cons = wrong_cons
        self.max_wrong = max_wrong
        self.wrong = 0
        self.correct_map = correct_map if correct_map is not None else [
            random.choice((0, 1)) for _ in scenes
        ]

    def play(self):
        """Run the scenes; return 'win' or 'lose'."""
        for i, scene in enumerate(self.scenes, start=1):
            self.ui.type_line(f'--- Room {i} of {len(self.scenes)} ---', delay=0.1)
            self.face.show(self.wrong)

            picked = self.ui.ask_choice(scene['prompt'], scene['options'][0], scene['options'][1])
            picked_text = scene['options'][picked]
            self.ui.type_line(f'You chose to "{picked_text}".')

            if picked == self.correct_map[i - 1]:
                consequence = random.choice(self.right_cons)
                self.ui.type_line(f'Now: {consequence}')
                self.ui.pulse_until_enter('>> Press Enter to continue <<')
                self.ui.print_blank()
            else:
                self.wrong += 1
                consequence = random.choice(self.wrong_cons)
                self.ui.type_line(f'Now: {consequence}')
                self.face.show(self.wrong)  # reveal more of the face
                if self.wrong >= self.max_wrong:
                    return "lose"
                self.ui.pulse_until_enter('>> Press Enter to continue <<')
                self.ui.print_blank()

        return "win"