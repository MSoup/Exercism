# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.wordProgress = ["_" for char in self.word]
        self.guessed = False
        self.charBank = ""

    def guess(self, char):
        if self.status != "ongoing":
            raise ValueError("Game not in operation")
        
        if char in self.charBank:
            self.remaining_guesses -= 1
            print("Please remember your guesses! -1 guess")
            
        for index, el in enumerate(self.word):
            if el == char:
                self.charBank += char
                self.wordProgress[index] = char
                #Set flag to True so guesses do not decrease
                self.guessed = True

        if self.guessed == False:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        elif "_" not in self.wordProgress:
            self.status = STATUS_WIN
            
        #Return guessed flag to False        
        self.guessed = False
        
    def get_masked_word(self):
        return "".join(self.wordProgress)

    def get_status(self):
        return self.status
