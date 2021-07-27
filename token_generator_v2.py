import random

# Main Routine

tokens = ["unicorn", "horse", "donkey", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE
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

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
