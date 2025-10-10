# ELEV B - Emmy

import sys, time                        # sys = skriva/läsa direkt i konsolen, time = pauser och klocka

# Använd Windows icke-blockerande tangentbord (blink medan vi väntar på Enter)
try:
    import msvcrt                       # msvcrt (finns på Windows) låter oss kolla tangenter utan att pausa
    HAS_MS = True                       # texten blinkar medan vi väntar på Enter
except Exception:
    HAS_MS = False                      # annars: ingen blink, vi använder vanlig input()

class UI:
    def __init__(self, type_delay=0.075, pulse_on_ms=500, pulse_off_ms=450):
        self.type_delay = type_delay    # hur lång paus per tecken i skrivmaskinen (sekunder)
        self.pulse_on_ms = pulse_on_ms  # hur länge texten är synlig vid blinkning (millisekunder)
        self.pulse_off_ms = pulse_off_ms # hur länge texten är dold vid blink (millisekunder)

    # Skrivmaskinen
    def type_line(self, text, delay=None):
        '''Skriv en rad tecken-för-tecken.'''
        d = self.type_delay if delay is None else delay   # använd standardhastighet om inget skickas in
        for ch in text:                                   # gå igenom varje tecken i texten
            print(ch, end='', flush=True)                 # skriv tecknet utan radbyte; flush=True = visa direkt
            time.sleep(d)                                 # vänta lite för skrivmaskin-känsla
        print()                                           # till sist: radbyte

    def type_lines(self, lines, delay=None):
        '''Skriv flera rader med skrivmaskin.'''
        d = self.type_delay if delay is None else delay   # samma hastighet för alla rader
        for line in lines:                                # gå igenom varje rad i listan
            self.type_line(line, delay=d)                 # skriv raden med skrivmaskin

    def print_blank(self):
        print()                                           # skriv en tom rad (mellanrum i utskriften)

    # Blinkade rad tills Enter
    def pulse_until_enter(self, msg):
        '''
        Visa 'msg' som blinkar på samma rad om och om igen
        tills användaren trycker Enter.
        '''
        if not HAS_MS:                                    # om vi inte kan blinka (t.ex. inte Windows-konsol)
            input('\n' + msg + ' ')                       # visa vanlig input-rad och vänta på Enter
            return                                        

        line = msg                                        # texten som ska blinka
        spaces = ' ' * len(line)                          # lika många mellanslag för att kunna "sudda" texten

        # NOTE: Ingen extra tom rad: vi skriver om samma rad med '\r' (gå till radens start)
        while True:
            # Visa texten (på)
            sys.stdout.write('\r' + line)                 # skriv texten från radens början
            sys.stdout.flush()                            # tvinga ut texten direkt på skärmen
            end = time.time() + self.pulse_on_ms / 1000.0 # när "på"-tiden ska vara slut (sekunder)
            while time.time() < end:                      # vänta tills "på"-tiden gått
                # msvcrt.kbhit() = finns en tangenttryckning redo?
                # msvcrt.getwch() = hämta den tangenten (Enter är '\r' eller '\n')
                if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                    sys.stdout.write('\r' + spaces + '\r\n') # rensa raden och gör ett radbyte
                    sys.stdout.flush()
                    return                                # klart: användaren tryckte Enter
                time.sleep(0.02)                          # kort paus så vi inte spinner CPU / # kort paus så vi inte använder 100% CPU

            # Dölj texten (av)
            sys.stdout.write('\r' + spaces + '\r')        # skriv mellanslag över samma rad (ser ut som att texten försvinner)
            sys.stdout.flush()
            end = time.time() + self.pulse_off_ms / 1000.0 # tidpunkt då "av"-fasen ska sluta
            while time.time() < end:                       # vänta tills "av"-tiden gått
                if msvcrt.kbhit() and msvcrt.getwch() in ('\r', '\n'):
                    sys.stdout.write('\r' + spaces + '\r\n') # sudda och radbyte
                    sys.stdout.flush()
                    return
                time.sleep(0.02)

    # Fråga om val (1 eller 2)
    def ask_choice(self, prompt_text, option1, option2):
        '''Fråga spelaren om 1 eller 2. Returenar 0 för första alternativet, 1 för andra.'''
        self.type_line(prompt_text, delay=self.type_delay) # fråga med skrivmaskin
        print(f"1) {option1}")                             # visa alternativ 1 direkt
        print(f"2) {option2}")                             # visa alternativ 2 direkt
        choice = input('> ').strip()                       # läs användarens svar och ta bort extra mellanslag
        while choice not in ('1', '2'):                    # om svaret inte är 1 eller 2
            print('Please type 1 or 2.')                   # be om ett giltigt svar
            choice = input('> ').strip()                   # läs igen
        return 0 if choice == '1' else 1                   # om '1' -> 0, annars -> 1