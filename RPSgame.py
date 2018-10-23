# Import the random package so that we can generate random numbers
from random import randint

# choices is an array ==> a containter that can hold multiple items.
# arrays are 0-based ==> the first item is 0, second is 1, etc.
# delcaration of variables!
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0, 2)]

# print the choice in the terminal window
print("Computer chooses: ", computer_choice)


while player is False:
    # give user options to pick
    print("choose your weapon!")
    player = input("Rock, Paper, or Scissors?\n")

    print(player, "\n")
    # if statements for game; tie
    if player == computer_choice:
        print("Tie! You live to shoot another day.")
    # if statement for user picking rock
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You Lose!", computer_choice, "covers", player)
        else:
            print("You win!", player, "smashes", computer_choice)
    # if statements for user choosing paper
    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You Lose!", computer_choice, "cuts", player)
        else:
            print("You win!", player, "covers", computer_choice)
    # if statements for user choosing scissots
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You Lose!", computer_choice, "smashes", player)
        else:
            print("You win!", player, "cuts", computer_choice)
    elif player == "Quit":
        exit()
    else:
        print("Check your spelling.. Not a valid choice.\n")
