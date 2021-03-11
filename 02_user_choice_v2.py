# Version 2 - error message included when calling function


# Functions go here
def choice_checker(question, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check that it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ",
                                 "Please choose from rock / paper / scissors (or 'xxx to quit)")

    # print out choice for comparison
    print("You chose {}".format(user_choice))
