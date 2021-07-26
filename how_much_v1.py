error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # Ask question
        how_much = int(input("How much would you like to play with? "))
        if 0 < how_much <= 10:
            print("You have asked to play with ${}".format(how_much))
        else:
            print(error)
    except ValueError:
        print(error)



