# ELEV B

import sys, time

# Try Windows non-blocking keyboard (so we can blink while waiting for Enter)
try:
    import msvcrt
    HAS_MS = True
except Exception:
    HAS_MS = False

class UI:
    def __init__(self, type_delay=0.075, pulse_on_ms=500, pulse_off_ms=450):
        self.type_delay = type_delay
        self.pulse_on_ms = pulse_on_ms
        self.pulse_off_ms = pulse_off_ms

    # ---- Your typewriter helpers ----
    def type_line(self, text, delay=None):
        """Print one line with typewriter effect (preserves your default behavior)."""
        d = self.type_delay if delay is None else delay
        for ch in text:
            print(ch, end='', flush=True)
            time.sleep(d)
        print()

    def type_lines(self, lines, delay=None):
        """Type out a list of lines."""
        d = self.type_delay if delay is None else delay
        for line in lines:
            self.type_line(line, delay=d)

    def print_blank(self):
        print()

    # ---- Your prompt ----
    def pulse_until_enter(self, msg):
        """Blink msg on one line until Enter is pressed (Windows: msvcrt; else plain input)."""
        if not HAS_MS:
            input('\n' + msg + ' ')
            return

        line = msg
        spaces = ' ' * len(line)

        # NOTE: no leading newline, exactly like your latest function
        while True:
            # Show
            sys.stdout.write('\r' + line); sys.stdout.flush()
            end = time.time() + self.pulse_on_ms / 1000.0
            while time.time() < end:
                if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                    sys.stdout.write('\r' + spaces + '\r\n'); sys.stdout.flush()
                    return
                time.sleep(0.02)

            # Hide
            sys.stdout.write('\r' + spaces + '\r'); sys.stdout.flush()
            end = time.time() + self.pulse_off_ms / 1000.0
            while time.time() < end:
                if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                    sys.stdout.write('\r' + spaces + '\r\n'); sys.stdout.flush()
                    return
                time.sleep(0.02)

    # ---- Your choice prompt (alternativen visas direkt) ----
    def ask_choice(self, prompt_text, option1, option2):
        """Ask the player to choose 1 or 2. Return 0 for first, 1 for second."""
        self.type_line(prompt_text, delay=self.type_delay)
        print(f"1) {option1}")
        print(f"2) {option2}")
        choice = input('> ').strip()
        while choice not in ('1', '2'):
            print('Please type 1 or 2.')
            choice = input('> ').strip()
        return 0 if choice == "1" else 1