INTRO = [
    'You wake on the cold tiles of a ruined hallway.',
    'Wind gnaws through cracked windows; A low, spectral hum floated through the air, too far to see yet too close to ignore.',
    'Somewhere in this house lies the Red Nursery — a room that should not exist.',
    'Every wrong turn draws you closer to its door.',
    'Every right turn leads toward a hidden exit, bricked up and buried under ivy.'
]

SCENES = [
    {
        'prompt': 'You stand in the hallway. What do you do?',
        'options': ('Light the wax candle', 'Follow the cold draft'),
    },
    {
        'prompt': 'A grand staircase presents itself, that later on splits itself in two. Where do you go?',
        'options': ('Go left', 'Go right'),
    },
    {
        'prompt': 'The library smells of mildew. Books covered in dust',
        'options': ('Pull the leather-strapped book', 'Lift the iron floor grate'),
    },
    {
        'prompt': 'The kitchen is dusted with flour. Footprints imprinted in the snow-like foundation. Something was here recently.',
        'options': ('Open the trapdoor by the stove', 'Crawl into the dumbwaiter'),
    },
    {
        'prompt': 'A narrow gallery. An eerie portrait of a woman. A plaque reads: THE NURSERY.',
        'options': ('Whisper the etched name', 'Cover the staring portrait'),
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