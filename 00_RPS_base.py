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

        if response == "rock" or response == "r":
            response = "rock"
            return response

        elif response == "paper" or response == "p":
            response = "paper"
            return response

        elif response == "scissors" or response == "sc":
            response = "scissors"
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

    if rounds_played == rounds - 1:
        end_game = "yes"

    choose_instruction = "Please choose rock (r) paper (p) or scissors (s) "
    print()
    choose_error = "Please choose from rock / paper / scissors (or 'xxx' to quit) "

    # Ask user for choice and check that it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # Get computer choice
    comp_choice = random.choice(rps_list[:-1])
        
    # Compare choices
    if comp_choice == user_choice:
        result = "tie"
    elif comp_choice == "rock" and user_choice == "paper":
        result = "won"
    elif comp_choice == "paper" and user_choice == "scissors":
        result = "won"
    elif comp_choice == "scissors" and user_choice == "rock":
        result = "won"
    else:
        result = "loss"

    if result == "tie":
        feedback = "It's a tie!"
    elif result == "won":
        feedback = " Congratulations you won!"
    else:
        feedback = "You lost (better luck next time)"

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    print("You chose: {}\nComputer chose: {}\n{}".format(user_choice, comp_choice, feedback))

    rounds_played += 1

# Ask user if they want to see their game history
# If 'yes' show game history

# Show game statistics
