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

        ###TOG BORT loopen som gjorde att den skrev ut alla stadier på ansiktet upp till nuvarande steg. Typ om jag hade svarat fel 2ggr så kom 3st ansikten upp. Genom att ta bort detta så printar den endast nuvarande ansikte för nuvarande steg.
        
        print(self.CREEPY_FACE[stage])