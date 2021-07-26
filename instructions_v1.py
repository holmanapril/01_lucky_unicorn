# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            instructions()
            return response

        else:
            print("Please answer yes or no")


def instructions():
    print("**** How to Play *****")
    print()
    print("The rules of the game go here")
    print()
    return""


# Main routine goes here...
played_before = yes_no("Have you played the game before?")
print("You chose {}".format(played_before))
print()
