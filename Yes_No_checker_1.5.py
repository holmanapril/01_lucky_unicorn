
# Ask the user if they have played before
played_before = input("Have you played before?")

# If they say yes, output "Program continues"
if played_before == "yes":
    print("Program continues")
elif played_before == "y":
    print("Program continues")
elif played_before == "yeah":
    print("Program continues")
elif played_before == "Y":
    print("Program continues")
elif played_before == "Yeah":
    print("Program continues")
elif played_before == "YeS":
    print("Program continues")
elif played_before == "yES":
    print("Program continues")

    # If they say no, output "display instructions"
elif played_before == "no":
    print("Display instructions")
elif played_before == "n":
    print("Display instructions")
elif played_before == "nah":
    print("Display instructions")
elif played_before == "N":
    print("Display instructions")
elif played_before == "Nah":
    print("Display instructions")
elif played_before == "NaH":
    print("Display instructions")
elif played_before == "NAH":
    print("Display instructions")

else:
    print("Please enter Yes or No")
    played_before = input("Have you played before?")
