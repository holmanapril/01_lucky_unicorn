import random

# Main Routine

STARTING_BALANCE = 100
balance = STARTING_BALANCE
# Testing Loop to generate 20 tokens
for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Change balance
    if 1 <= chosen_num <= 7:
        chosen = "unicorn"
        balance += 4
    elif 8 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
            balance -= 0.5
    print("Token:{} , Balance = ${}".format(chosen, balance))

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
