import random
from game_art import logo, vs
from game_data import data


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = random.choice(data)
    account_b = random.choice(data)
    while game_should_continue:
        while account_a == account_b:
            account_b = random.choice(data)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
        my_guess = input("Who has more followers! Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_corect = check_answer(my_guess, a_follower_count, b_follower_count)
        if is_corect:
            if my_guess == "a":
                account_a = account_a
                account_b = random.choice(data)
            else:
                account_a = account_b
                account_b = random.choice(data)
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
