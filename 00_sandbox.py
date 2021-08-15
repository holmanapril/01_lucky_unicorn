import random


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")


def instructions():
    print("**** How to Play *****")
    print()
    print("Choose a starting amount (minimum $1, maximum $10).")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win some money back. Here's the payout amounts...\n"
          "Unicorn: $5 (balance increases by $4)\n"
          "Zebra: $0.50 (balance decreases by $0.50)\n"
          "Horse: $0.50 (balance decreases by $0.50)\n"
          "Donkey: $0.00 (balance decreases by $1)")
    return""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask question
            response = int(input(question))
            if low < response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def lucky_unicorn_greeting():
    greeting = "Welcome to the Lucky Unicorn Game"
    sides = "*" * 3

    greeting = "{} {} {}".format(sides, greeting, sides)

    top_bottom = "*" * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)


def unicorn_tokens():
    unicorn_token = "Congratulations you got a Unicorn "
    sides = "!" * 3

    unicorn_token = "{} {} {}".format(unicorn_sides, unicorn_token, unicorn_sides)

    unicorn_top_bottom = "!" * len(unicorn_token)

    print(unicorn_top_bottom)
    print(unicorn_token)
    print(unicorn_top_bottom)
    print()


def zebra_tokens():
    zebra_token = " You got a Zebra "
    zebra_sides = "z" * 3

    zebra_token = "{} {} {}".format(zebra_sides, zebra_token, zebra_sides)

    zebra_top_bottom = "z" * len(zebra_token)

    print(zebra_top_bottom)
    print(zebra_token)
    print(zebra_top_bottom)
    print()


def horse_tokens():
    horse_token = " You got a Horse "
    horse_sides = "h" * 3

    horse_token = "{} {} {}".format(horse_sides, horse_token, horse_sides)

    horse_top_bottom = "h" * len(horse_token)

    print(horse_top_bottom)
    print(horse_token)
    print(horse_top_bottom)
    print()


def donkey_tokens():
    donkey_token = " You got a Donkey "
    donkey_sides = "d" * 3

    donkey_token = "{} {} {}".format(donkey_sides, donkey_token, donkey_sides)

    donkey_top_bottom = "d" * len(donkey_token)

    print(donkey_top_bottom)
    print(donkey_token)
    print(donkey_top_bottom)


# Main Routine goes here

lucky_unicorn_greeting()
print()
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play").lower()
while play_again == "":
    # Loop
    rounds_played += 1

    # Print round number
    print()
    print("*** Round {} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Change balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        unicorn_tokens()
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        donkey_tokens()
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            horse_tokens()
            balance -= 0.5
        else:
            chosen = "zebra"
            zebra_tokens()
            balance -= 0.5
    print("Token:{} , Balance = ${}".format(chosen, balance))
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or xxx to quit")

print()
print("Final Balance: ${:.2f}".format(balance))
print()
print("Thanks for playing")
