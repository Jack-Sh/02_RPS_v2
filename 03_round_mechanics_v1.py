# Function
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please enter an integer greater than 0"
        response = int(response)

        if response < 1:
            print(round_error)
            continue

        else:
            continue

    return response


# Main routine
rounds_played = 0
choose_instruction = "Please choose rock (r) paper (p) or scissors (s) "

# Ask user for # of rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    heading = "Round {} of {}".format(rounds_played +1, rounds)
    print(heading)
    choose = input(choose_instruction)
    if rounds_played == rounds - 1:
        end_game = "yes"

    # Rest of loop / game
        print("You chose {}".format(choose))

        rounds_played += 1

print("Thank you for playing!")
