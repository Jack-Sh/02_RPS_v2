import random

game_summary = []

# Functions go here


# Number checking function, response must be an integer more than 0
# also accepts <enter> for infinite rounds
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


# Choice checker function, response must be out of a specified valid list
# also works for the first letter of the word
def choice_checker(question, valid_list, error,):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        else:
            print(error)


# Functions to display instructions when called
def instructions():
    print()
    statement_generator("How to Play", "*")
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
    statement_generator("Have Fun", "*")


# Function to print five symbols / emojis on either side of specified statements
def statement_generator(statement, decoration):

    sides = decoration * 5
    statement = "{} {} {}".format(sides, statement, sides)

    print(statement)

    return ""


# Main routine goes here


# Lists of valid responses to be used when calling choice_checker function
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
statement_generator("Welcome to the RPS Game", "*")
print()
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# If 'no' show instructions
if played_before_response == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0

rounds_lost = 0
rounds_drawn = 0
rounds_won = 0

# Game heading (prints after users answer the 'played_before' question
print()
statement_generator("Let's Get Started", "!")
print()

# Displays at the start of every round
choose_instruction = "Please choose rock (r) paper (p) or scissors (s) "

# Ask user for # of rounds
rounds = check_rounds()

# Game looping mechanics
end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    # if the user enters <enter> the continuous rounds heading displays
    # if user enters a valid integer it displays how many rounds you have
    # played out of the rounds chosen
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)

    if rounds_played == rounds:
        break

    # Prints heading with decoration
    statement_generator(heading, "-")

    # errors
    choose_instruction = "Please choose rock (r) paper (p) or scissors (s) "
    print()
    choose_error = "Please choose from rock / paper / scissors (or 'xxx' to quit)\n"

    # Ask user for choice and check that it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # Get computer choice (minus xxx from rps_list)
    comp_choice = random.choice(rps_list[:-1])

    # End game if exit code is typed if user has played more than 1 round
    if user_choice == "xxx" and rounds_played > 0:
        break

    # If user hasn't played one round
    # display an error and start from beginning
    elif user_choice == "xxx" and rounds_played == 0:
        print("You need to play at least one round!")
        continue

    # Compare user_choice with comp_choice
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

    # Justify results and give feedback
    if result == "tie":
        feedback = "It's a tie!"
        rounds_drawn += 1
        statement_decoration = "👔"

    elif result == "won":
        feedback = "Congratulations you won"
        rounds_won += 1
        statement_decoration = "🏆"

    else:
        feedback = "You lost (better luck next time)"
        rounds_lost += 1
        statement_decoration = "❌"

    # if the result is a loss or a win print 'you lost' or 'you won'
    # if the result is a tie print 'it's a tie'
    # (for game history)
    if result == "lost" or result == "won":
        outcome = "Round {}: {} vs {} - you {}".format(rounds_played + 1, user_choice, comp_choice, result)
    else:
        outcome = "Round {}: {} vs {} - it's a {}".format(rounds_played + 1, user_choice, comp_choice, result)

    game_summary.append(outcome)

    # output both choices and feedback after every round
    print("You chose: {}\nComputer chose: {}".format(user_choice, comp_choice,))

    # Decoration for feedback
    statement_generator(feedback, statement_decoration)

    # Add one round to total rounds played
    rounds_played += 1

# Ask user if they want to see their game history
game_history = "Do you want to see your game history? "
game_history_response = choice_checker(question=game_history,
                                       valid_list=yes_no_list,
                                       error="Please enter yes or no")

# If 'yes' show game history
if game_history == "yes":
    print()
    statement_generator("Game History", "=")
    for game in game_summary:
        print(game)

# Calculate game stats in percentages
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_drawn = rounds_drawn / rounds_played * 100

# Show game statistics in percentages and number of W / L / D
print()
print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%)\nLoss {}, ({:.0f}%)\nDraw {}, ({:.0f}%)"
      .format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_drawn))

# End of game statements
print()
statement_generator("Thanks for Playing", "!")
