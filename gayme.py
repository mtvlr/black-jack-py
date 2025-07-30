import random


def new_deck():
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    random.shuffle(cards) 
    return cards

print(new_deck())

