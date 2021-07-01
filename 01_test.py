#name = input("Hello, what is your name?")
#fruit = input("Pick a fruit")
#food = input("What is your favourite food?")
#animal = input("Pick an animal")
#animal_name = input("Give it a name")

#print("Hi {} guess what? {} the {} is eating some {} and your {}".format(name, animal_name, animal, fruit, food))

#Setting score and lives variables
score = 0
lives =5
highscore = 0

#Question 1
answer_1 = input("What country is the Unicorn native to?")
answer_1 = answer_1.strip().title()
if answer_1 == "Scotland":
    print("That is correct")
    score += 1
else:
    print("That is incorrect, the Unicorn is actually native to Scotland")
    lives -= 1

#Question 2
while True:
    try:
        answer_2 = float(input("How many miles away from a Blue Whale can you hear its heartbeat?"))
        break
    except ValueError:
        print("Please enter a valid number")
if answer_2 == 2:
    print("That is correct")
    score += 1
else:
    print("That is incorrect, the answer is actually 2 miles")
    lives -= 1

#Question 3
answer_3 = input("What is a baby puffin called?")
answer_3 = answer_3.strip().title()
if answer_3 == "Puffling":
    print("That is correct")
    score += 1
else:
    print("That is incorrect, the answer is Puffling")
    lives -= 1

#Question 4
while True:
    try:
        answer_4 = int(input ("How many grapes are needed to make 1 bottle of wine?"))
        break
    except ValueError:
        print("Please enter a valid number")

if answer_4 == 700:
    print("That is correct")
    score += 1
else:
    print("That is incorrect, the answer is actually 700 grapes")
    lives -= 1

#Question 5
while True:
    try:
        answer_5 = int(input("How many million American Hotdogs do Americans eat on the 4th of July?"))
        break
    except ValueError:
        print("Please enter a valid number")

if answer_5 == 150:
    print("That is correct")
    score += 1
else:
    print("That is incorrect,the answer was 150 million")
    lives -= 1
    for lives in range(0):
        break






