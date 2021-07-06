played_before = ""
while played_before != "xxx":

    # Ask the user if they have played before
    played_before = input("Have you played before?").strip().lower()

    # If they say yes, output "Program continues"
    if played_before == "yes":
        print("Program continues")
    elif played_before == "y":
        print("Program continues")
    elif played_before == "yeah":
        print("Program continues")

        # If they say no, output "display instructions"
    elif played_before == "no":
        print("Display instructions")
    elif played_before == "n":
        print("Display instructions")
    elif played_before == "nah":
        print("Display instructions")

    else:
        print("Please enter Yes or No")
        played_before = input("Have you played before?")
        played_before = played_before.strip().lower()
