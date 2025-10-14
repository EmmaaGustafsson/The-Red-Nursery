import time

class CreepyFace:
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
        stage = wrong_count
        if stage < 0:
            stage = 0
        if stage > len(self.CREEPY_FACE) - 1:
            stage = len(self.CREEPY_FACE) - 1

        
        for i in range(stage + 1):
            print(self.CREEPY_FACE[i])
            time.sleep(0.5) 
        
        print(self.CREEPY_FACE[stage])