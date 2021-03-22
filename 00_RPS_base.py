import random

game_summary = []

# Functions go here


def check_rounds():
    while True:
        # Ask user how many rounds
        response = input("How many rounds: ")

        round_error = "Please enter an integer greater than 0"

        # If user DOESN'T type <enter> check to see
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
            if response == item[1] or response == item:
                return response

        if response == "rock" or response == "r":
            response = "rock"
            return response

        elif response == "paper" or response == "p":
            response = "paper"
            return response

        elif response == "scissors" or response == "s":
            response = "scissors"
            return response

        # check for exit code...
        elif response == "xxx":
            return response

        else:
            print(error)


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter either Yes or No")


def instructions():
    print()
    print("***** How to Play *****")
    print()
    print("Choose either a number of rounds or press <enter> for continuous mode")
    print()
    print("Then for each round choose between:")
    print("rock, paper, scissors (or 'xxx' to quit)")
    print("You can also type r / p / s (instead of the whole word)")
    print()
    print("The rules are...")
    print("- Rock beats scissors")
    print("- Paper beats rock")
    print("- Scissors beats paper")
    print()
    print("***** Have Fun! *****")


# Main routine goes here


# Lists of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
played_before = yes_no("Have you played the game before? ")

# If 'no' show instructions
if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0

rounds_lost = 0
rounds_drawn = 0
rounds_won = 0

# Game heading
print()
print("***** Let's Get Started! *****")
print()

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

    if rounds_played == rounds:
        break

    print(heading)

    # errors
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
        result = "lost"

    if result == "tie":
        feedback = "It's a tie!"
        rounds_drawn += 1

    elif result == "won":
        feedback = "Congratulations you won!"
        rounds_won += 1

    else:
        feedback = "You lost (better luck next time)"
        rounds_lost += 1

    # End game if exit code is typed
    if user_choice == "xxx":
        rounds_lost -= 1
        break

    # if the result is a loss or a win print 'you lost' or 'you won'
    # if the result is a tie print 'it's a tie'
    if result == "lost" or result == "won":
        outcome = "Round {}: {} vs {} - you {}".format(rounds_played + 1, user_choice, comp_choice, result)
    else:
        outcome = "Round {}: {} vs {} - it's a {}".format(rounds_played + 1, user_choice, comp_choice, result)

    game_summary.append(outcome)

    # output both choices and feedback
    print("You chose: {}\nComputer chose: {}\n{}".format(user_choice, comp_choice, feedback))

    rounds_played += 1

# Ask user if they want to see their game history
game_history = yes_no("Do you want to see the game history? ")

# If 'yes' show game history
if game_history == "yes":
    print()
    print("***** Game History *****")
    for game in game_summary:
        print(game)

# Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_drawn = rounds_drawn / rounds_played * 100

# Show game statistics
print()
print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%)\nLoss {}, ({:.0f}%)\nDraw {}, ({:.0f}%)"
      .format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_drawn))

# End of game statements
print()
print("Thanks for Playing!")
