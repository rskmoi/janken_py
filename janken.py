import random
from enum import IntEnum

HAND = {0: "Guu", 1: "Choki", 2: "Paa"}

class Status(IntEnum):
    DRAW = 0
    LOSE = 1
    WIN = 2

class Player:
    def __init__(self, name):
        self.name = name

    def get_hand(self):
        return random.randint(0, 2)

def judge(hand1, hand2):
    status = Status(((hand1 - hand2) + 3) % 3)
    return status

def play_one_game(player1, player2):
    hand1 = player1.get_hand()
    hand2 = player2.get_hand()
    status = judge(hand1, hand2)
    print("{}: {}, {}: {}, {}'s status is {}".format(player1.name, HAND[hand1],
                                                     player2.name, HAND[hand2],
                                                     player1.name, str(status)))
    if status == Status.DRAW:
        status = play_one_game(player1, player2)

    return status

if __name__ == '__main__':
    player1 = Player("A")
    player2 = Player("B")
    _ = play_one_game(player1, player2)
