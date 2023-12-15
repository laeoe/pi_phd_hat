from pi_phd_hat.pi_piano import PiPiano

test_sequence = [[60, 72], [62, 74], [64, 76], [65, 77], [67, 79], [69, 81], [71, 83], [72, 84]]



class Play_correct_sequence:
    def __init__(self, sequence_to_play: list):
        self.progress = 0
        self.piano = PiPiano(piano_callback=self.callback_function, verbose=False)
        self.sequence_1 = sequence_to_play
        self.next_element = self.sequence_1[self.progress].copy()


    def advance_progress(self):
        self.progress += 1
        print(f"Advancing progress, current progress is {self.progress}")
        if self.is_complete():
            self.finish()
        
        else:
            self.next_element = self.sequence_1[self.progress].copy()
            print(f"Progress is now {self.progress}, next element is {self.next_element}")
        

    def check_sequence(self, note):
        if note in self.next_element:
            # print(f"Played correct note {note}, from expected {self.next_element}")
            # remove the not from next_element
            self.next_element.remove(note)
            if len(self.next_element) == 0:
                self.advance_progress()
        else:
            print(f"played {note} but expecting {self.next_element}, resetting")
            self.reset()
    
    def callback_function(self, note, is_pressed, msg):
        if is_pressed:
            self.check_sequence(note)
        if not is_pressed:
            ...        # print(f'callback function called, got note {note} of type {type(note)}')


    def start(self):
        print(f"Starting level 1, playing sequence {self.sequence_1}, next element is {self.next_element}")
        self.piano.start()


    def is_complete(self)->bool:
        if self.progress >= len(self.sequence_1):
            # print("completness check true")
            return True
        else:
            return False

    def finish(self):

        print("\n###############")
        print("Level Won")
        print("###############\n")
        self.reset()
        self.piano.close()
        # exit()
        # raise something to exit 
        raise KeyboardInterrupt # this is a hack, but it works


    def reset(self):
        self.progress = 0
        self.next_element = self.sequence_1[self.progress].copy()




if __name__ == "__main__":
    song_topolino = [[76], [74], [76], [74], [76], [77], [76], [72], [72], [72], [72]] 
    level1 = Play_correct_sequence([[60]])
    try:
        level1.start()
    except KeyboardInterrupt:
        pass


    
    