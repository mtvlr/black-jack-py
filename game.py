import random


def new_deck():
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    cards = cards * 4
    random.shuffle(cards) 
    return cards

def get_bet():
    while True:
        user_input = input("Please make your bet: ")
        if user_input.isdigit():
            return int(user_input)
        print("Not valid format")

def card_value(karta1):
    if karta1.isnumeric():
        return int(karta1)
    if karta1 == "Jack" or "Queen" or "King":
        return 10
    if karta1 == "Ace":
        return 11

chips = 100
diler = 0
player = 0
bet = get_bet()

deck = new_deck()
chips = chips - bet

while player < 21 and diler < 21:
    karta1 = deck.pop() 
    karta2 = deck.pop()
    player = player + card_value(karta1)
    diler = diler + card_value(karta2)
    print(karta1, karta2, player, diler)

if player > 21 or (player < diler and diler < 21): 
    print("You lost. You have ")
    print(chips)

elif player == 21 and diler == 21:
    print("Tie. You have ")
    chips = chips + bet
    print(chips)

else:
    print("You won. You have ")
    chips = chips + bet + bet
    print(chips)

