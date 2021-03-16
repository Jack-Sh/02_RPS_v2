rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options...
        if comp_choice == "rock" and user_choice == "rock":
            result = "tie"
        elif comp_choice == "paper" and user_choice == "paper":
            result = "tie"
        elif comp_choice == "scissors" and user_choice == "scissors":
            result = "tie"
        elif comp_choice == "rock" and user_choice == "paper":
            result = "won"
        elif comp_choice == "paper" and user_choice == "scissors":
            result = "won"
        elif comp_choice == "scissors" and user_choice == "rock":
            result = "won"
        elif comp_choice == "rock" and user_choice == "scissors":
            result = "loss"
        elif comp_choice == "paper" and user_choice == "rock":
            result = "loss"
        elif comp_choice == "scissors" and user_choice == "paper":
            result = "loss"

        print("You chose {}, the computer chose {}. \n"
              "Result: {}".format(user_choice, comp_choice, result))
        print()

    comp_index += 1
