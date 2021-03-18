# Version 3 - checks that response is given in a list


# Functions go here
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        if response == "r" or response == "rock":
            response = "rock"
            return response
        elif response == "p" or response == "paper":
            response = "paper"
            return response
        elif response == "s" or response == "scissors":
            response = "scissors"
            return response

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine goes here


# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check that it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list,
                                 "Please choose from rock / paper / scissors (or 'xxx to quit)")

    # print out choice for comparison
    print("You chose {}".format(user_choice))
