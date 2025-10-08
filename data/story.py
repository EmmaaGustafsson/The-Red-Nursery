# ELEV C

INTRO = [
    'You wake on the cold tiles of a ruined foyer.',
    'Wind gnaws through cracked windows; a chandelier sways without a breeze.',
    'Somewhere in this house lurks the Red Nursery — a room that should not exist.',
    'Every wrong turn draws you closer to its door.',
    'Every right turn leads toward a hidden exit, bricked up and buried under ivy.'
]

SCENES = [
    {
        'prompt': 'You stand in the foyer. What do you do?',
        'options': ('Light the wax candle', 'Follow the cold draft'),
    },
    {
        'prompt': 'A grandfather clock ticks out of time. The hall splits.',
        'options': ("Slip into the servants' passage", 'Take the grand staircase'),
    },
    {
        "prompt": "The library smells of mildew.",
        "options": ("Pull the leather-strapped book", "Lift the iron floor grate"),
    },
    {
        'prompt': 'A narrow gallery. A plaque reads: THE NURSERY.',
        'options': ('Whisper the etched name', 'Cover the staring portrait'),
    },
    {
        'prompt': 'The kitchen is dusted with flour. Something moved recently.',
        'options': ('Open the trapdoor by the stove', 'Crawl into the dumbwaiter'),
    },
    {
        'prompt': 'Child-sized hallway. A rose-colored door waits.',
        'options': ('Turn the porcelain knob', 'Back toward the ivy-choked door'),
    },
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