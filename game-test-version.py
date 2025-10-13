import time
import random
import sys

# Try windows non-blocking keyboard (so we can blink while waiting for Enter)
try:
    import msvcrt
    HAS_MS = True
except Exception:
    HAS_MS = False

# ---------------- Settings you can tweak ----------------
TYPE_DELAY = 0.075   # seconds per character (make smaller to go faster)
MAX_WRONG  = 3       # how many mistakes before GAME OVER
PULSE_ON_MS = 500    # visible time
PULSE_OFF_MS = 450   # hidden time
# --------------------------------------------------------

# ------------- CLASS IMPLEMENTATION ---------------------
class CreepyFace:
    #Class that represents the creepy face that becomes more complete for every mistake
    def __init__(self):
        self.stages = [
            '''
                
                x   o
                
            ''',
            '''
               ( o   )
                
            ''',
            r'''
               (   x )
                \_ _/
            ''',
            r'''
               ( x x )
                \_-_/
               /| | |\
            '''
        ]
        self.wrong_count = 0

    def show(self):
        # Display the current stage of the creepy face
        stage = min(self.wrong_count, len(self.stages) - 1)
        print(self.stages[stage])

    def increment(self):
        # Increase wrong count to progress the face
        self.wrong_count += 1

# ------------------- Helper functions --------------------
def type_out(text, delay=TYPE_DELAY):
    """Print text with a simple typewriter effect."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()  # newline at the end

def type_lines(lines, delay=TYPE_DELAY):
    """Type out a list of lines."""
    for line in lines:
        type_out(line, delay)

def pulse_until_enter(msg):
    """Blink msg on one line until Enter is pressed (Windows: msvcrt; else plain input)."""
    if not HAS_MS:
        input('\n' + msg + ' ')
        return

    line = msg
    spaces = ' ' * len(line)

    while True:
        # Show
        sys.stdout.write('\r' + line); sys.stdout.flush()
        end = time.time() + PULSE_ON_MS / 1000.0
        while time.time() < end:
            if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                sys.stdout.write('\r' + spaces + '\r\n'); sys.stdout.flush()
                return
            time.sleep(0.02)


        # Hide
        sys.stdout.write('\r' + spaces + '\r'); sys.stdout.flush()
        end = time.time() + PULSE_OFF_MS / 1000.0
        while time.time() < end:
            if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                sys.stdout.write('\r' + spaces + '\r\n'); sys.stdout.flush()
                return
            time.sleep(0.02)

# ----------- Story (texts) -----------
INTRO = [
    'You wake on the cold tiles of a ruined foyer.',
    'Wind gnaws through cracked windows; a chandelier sways without a breeze.',
    'Somewhere in this house lurks the Red Nursery — a room that should not exist.',
    'Every wrong turn draws you closer to its door.',
    'Every right turn leads toward a hidden exit, bricked up and buried under ivy.'
]

SCENES = [
    {'prompt': 'You stand in the foyer. What do you do?',
     'options': ('Light the wax candle', 'Follow the cold draft')},
    {'prompt': 'A grandfather clock ticks out of time. The hall splits.',
     'options': ("Slip into the servants' passage", 'Take the grand staircase')},
    {"prompt": "The library smells of mildew.",
     "options": ("Pull the leather-strapped book", "Lift the iron floor grate")},
    {'prompt': 'A narrow gallery. A plaque reads: THE NURSERY.',
     'options': ('Whisper the etched name', 'Cover the staring portrait')},
    {'prompt': 'The kitchen is dusted with flour. Something moved recently.',
     'options': ('Open the trapdoor by the stove', 'Crawl into the dumbwaiter')},
    {'prompt': 'Child-sized hallway. A rose-colored door waits.',
     'options': ('Turn the porcelain knob', 'Back toward the ivy-choked door')}
]

WIN_TEXT = [
    'The ivy parts over damp brick. A hidden gate grinds open to the night garden.',
    'Behind you, the house exhales — disappointed — as you step outside.',
    'YOU ESCAPED.'
]

LOSE_TEXT = [
    'The door swings inward to a room the house kept warm.',
    'A cradle rocks itself. Tiny fingernail scratches score the walls.',
    'The lullaby begins behind your ear.',
    'THE RED NURSERY FOUND YOU.'
]

RIGHT_CONSEQUENCES = [
    'A hidden bolt slides somewhere.',
    'The floor relaxes beneath your feet.',
    "Keys jingle in a room you can't see.",
    'The draft changes direction.'
]

WRONG_CONSEQUENCES = [
    "Wallpaper peels toward a child's door.",
    'The air warms, like breath on your neck.',
    'Floorboards tilt toward the Red Nursery.',
    'A lullaby thread pulls you down the wrong hall.'
]

# -------------------- Game loop --------------------
def ask_choice(prompt_text, option1, option2):
    """Ask the player to choose 1 or 2. Return 0 for first, 1 for second."""
    type_out(prompt_text)
    print(f"1) {option1}")
    print(f"2) {option2}")
    choice = input('> ').strip()
    while choice not in ('1', '2'):
        print('Please type 1 or 2.')
        choice = input('> ').strip()
    return 0 if choice == "1" else 1

def main():
    # Initialize
    correct_map = [random.choice((0, 1)) for _ in SCENES]
    face = CreepyFace()

    # Title + intro
    type_out('HAUNTED HOUSE: The Red Nursery', delay=0.1)
    type_lines(INTRO, delay=TYPE_DELAY)
    pulse_until_enter('>> Press Enter to begin <<')
    print()

    # Main loop
    for i, scene in enumerate(SCENES, start=1):
        type_out(f'--- Room {i} of {len(SCENES)} ---', delay=0.1)
        face.show()

        picked = ask_choice(scene['prompt'], scene['options'][0], scene['options'][1])
        picked_text = scene['options'][picked]
        type_out(f'You chose to "{picked_text}".')

        if picked == correct_map[i - 1]:
            consequence = random.choice(RIGHT_CONSEQUENCES)
            type_out(f'Now: {consequence}')
            pulse_until_enter('>> Press Enter to continue <<')
            print()
        else:
            face.increment()
            consequence = random.choice(WRONG_CONSEQUENCES)
            type_out(f'Now: {consequence}')
            face.show()
            if face.wrong_count >= MAX_WRONG:
                print()
                type_lines(LOSE_TEXT, delay=TYPE_DELAY)
                pulse_until_enter('YOU DIED')
                return
            pulse_until_enter('>> Press Enter to continue <<')
            print()

    # Win
    print()
    type_lines(WIN_TEXT, delay=TYPE_DELAY)
    pulse_until_enter('YOU SURVIVED')

if __name__ == '__main__':
    main()
