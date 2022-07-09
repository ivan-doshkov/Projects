import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_score = 0
dealer_score = 0
my_cards = []
dealer_cards = []


def my_hit(cards1):
    return my_cards.append(random.choice(cards1))


def dealer_hit(cards2):
    return dealer_cards.append(random.choice(cards2))


for i in range(2):
    my_hit(cards)
    my_score = sum(my_cards)
print(f"Your cards: {my_cards}, current score: {my_score}")
dealer_hit(cards)
dealer_score = sum(dealer_cards)
print(f"Dealer's first card: {dealer_cards}")

while True:

    if my_score == 21:
        print("BLACK JACK!\n"
              "You Win!")
        break
    comand = input("Type 'y' to get another card, type 'n' to pass: ")
    if my_score < 21:
        if comand == "y":
            my_hit(cards)
            my_score = sum(my_cards)
            print(f"Your cards: {my_cards}, current score: {my_score}")
            if my_score > 21:
                for card in my_cards:
                    if card == 11:
                        if my_score > 21:
                            my_cards.remove(11)
                            my_cards.append(1)
                            my_score = sum(my_cards)
                    else:
                        print("Dealer Win!")
                        break
            if my_score == 21:
                dealer_hit(cards)
                dealer_score = sum(dealer_cards)
                print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")
                if dealer_score < my_score or dealer_score > 21:
                    print("You Win!")
                    break
                else:
                    print("Draw!")
    if comand == "n":
        dealer_hit(cards)
        dealer_score = sum(dealer_cards)
        print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")

        if dealer_score == 21:
            print("Dealer has a Black Jack!")
            print("Dealer Win!")
            break
        while dealer_score < 17:
            dealer_hit(cards)
            dealer_score = sum(dealer_cards)
            print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")
            if dealer_score > 21:
                for card in dealer_cards:
                    if card == 11:
                        dealer_cards.remove(11)
                        dealer_cards.append(1)
                        dealer_score = sum(dealer_cards)
                        if dealer_score < 17:
                            dealer_hit(cards)
                            dealer_score = sum(dealer_cards)
                    elif card != 11 and dealer_score > 21:
                        print("You Win!")
                        break
            if dealer_score == 21 and my_score < 21:
                print("Dealer Win!")
                break
            if my_score < (17 <= dealer_score) < 21:
                print("Dealer Win!")
                break
        if 17 <= dealer_score <= 20:
            if my_score == dealer_score:
                print("Draw!")
                break
            if dealer_score < my_score:
                print("You Win!")
                break
            else:
                print("Dealer Win!")
                break
        break
