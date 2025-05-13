import random

class Game():
    def __init__(self):
        self.history = 0
        self.wins = 0
        self.losts = 0
        self.draws = 0
    hands_dict = {1 : "rock", 2 : "paper", 3 : "scissors"}
    def play(self, hand):
        self.history += 1
        computer_hand = random.randint(1, 3)
        print(computer_hand)
        if hand == 1 and computer_hand == 3:
            print("you chose rock and computer chose scissors, you win :)")
            self.wins += 1
        elif hand > computer_hand :
            print(f"you chose {self.hands_dict[hand]} and computer chose {self.hands_dict[computer_hand]}, you win :)")
            self.wins += 1
        elif hand == computer_hand:
            print(f"you both chose {self.hands_dict[hand]}, it's a draw :|")
            self.draws += 1
        else:
            print(f"you chose {self.hands_dict[hand]} and computer chose {self.hands_dict[computer_hand]}, you lose :(")
            self.losts += 1