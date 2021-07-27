import random

# Main Routine

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100
# Testing Loop to generate 20 tokens
for item in range(0, 100):
    chosen = random.choice(tokens)

    # Change balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # Print out results and balance
    print("Token:{} , Balance = ${}".format(chosen, balance))
