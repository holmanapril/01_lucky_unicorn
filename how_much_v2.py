# Functions
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


# Main Routine
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have asked to play with ${}".format(how_much))
