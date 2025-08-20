import random


def new_deck():
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
    cards = cards * 4
    random.shuffle(cards) 
    return cards


def get_bet():
    while True:
        user_input = input("Please make your bet: ")
        if user_input.isdigit():
            return int(user_input)
        print("Not valid format")


def card_value(karta1, player):
    if karta1.isnumeric():
        return int(karta1)
    if karta1 == "Jack" or karta1 == "Queen" or karta1 == "King":
        return 10
    if karta1 == "Ace":
        if player > 10:
            return 1
        return 11


def blackjack():
    player = 0
    diler = 0
    deck = new_deck()
    
    print("Player's hand")
    karta1 = deck.pop()
    karta2 = deck.pop()
    player = player + card_value(karta1, player) 
    player = player + card_value(karta2, player)
    print("First card: ", karta1, "Second card: ",  karta2, "Total: ", player)
    
    print("Diler's hand")
    karta1 = deck.pop()
    karta2 = deck.pop()
    diler = diler +  card_value(karta1, diler) 
    diler = diler + card_value(karta2, diler)
    print("First card: ", karta1, "Second card: ",  karta2, "Total: ", diler)
    print()

    
    while player < 21:
        while True:
            user_choice = input("Please make your choice (Hit|Stand): ")
            if user_choice == "hit":
                karta1 = deck.pop()
                player = player + card_value(karta1, player)
                print("Card: ", karta1, "Total", player)
                break

            elif user_choice == "stand":
                print("Pass")
                break
            
            else:
                print("Not valid format") 

        if user_choice == "stand":
            break
         
    if player > 21:
        return "Lose"
    
    elif player == 21: 
        print("Natural blackjack!")

    while diler < 17:
        karta1 = deck.pop()
        diler = diler + card_value(karta1, diler)
        print("Card: ", karta1, "Total: ", diler)
    
    if  player < diler and diler <= 21: 
        return "Lose"

    elif player == 21 and diler == 21:
        return "Tie"

    return "Win"
    



def main():
    chips = 100
    while chips > 0:
        bet = get_bet()

        chips = chips - bet

        dolg = blackjack()

        if dolg == "Lose": 
            print("You lost. You have ")
            print(chips)

        elif dolg == "Tie":
            print("Tie. You have ")
            chips = chips + bet
            print(chips)

        elif dolg == "Win":
            print("You won. You have ")
            chips = chips + bet + bet
            print(chips)
    
    if chips < 0:
        print("You own us money! Sell everything and give money back")
        return

    print("You have gambled all your money, now you own us a lot of money, sell the house! ")

main()
