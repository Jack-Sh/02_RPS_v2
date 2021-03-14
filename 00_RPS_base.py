import random

# Functions go here


def check_rounds():
    while True:
        # Ask user how many rounds
        response = input("How many rounds: ")

        round_error = "Please enter an integer greater than 0"

        # If user DOESN'T type enter check to see
        # if it is a valid integer

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            # If the user doesn't type a valid response
            # print an error message (program won't break)

            except ValueError:
                print(round_error)
                continue

        return response


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


# Lists of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'no' show instructions

# Ask user for # of rounds then loop...
rounds_played = 0
choose_instruction = "Please choose rock (r) paper (p) or scissors (s) "

# Ask user for # of rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{}or 'xxx' to end: ".format(choose_instruction))

    # Ask user for choice and check that it's valid
    choose = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list,
                                 "Please choose from rock / paper / scissors (or 'xxx to quit)")

    # End game if exit code is typed
    if choose == "xxx":
        break

    print("You chose {}".format(choose))

    rounds_played += 1

# Ask user if they want to see their game history
# If 'yes' show game history

# Show game statistics
