# ELEV C

class CreepyFace:
    """Simple creepy face with 4 stages (0..3) — unchanged from your code."""

    CREEPY_FACE = [
        '''
            
             x o
            
        ''',
        '''
           ( o x )
            
        ''',
        r'''
           ( x o )
            \_ _/
        ''',
        r'''
           ( x x )
            \_-_/
           /| | |\
        '''
    ]

    def show(self, wrong_count):
        """Show the current stage of the creepy face based on wrong choices."""
        stage = wrong_count
        if stage < 0: stage = 0
        if stage > 3: stage = 3
        print(self.CREEPY_FACE[stage])