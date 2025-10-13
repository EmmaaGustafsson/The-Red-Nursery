class CreepyFace:
    # Class that represents the creepy face that becomes more complete for every mistake
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