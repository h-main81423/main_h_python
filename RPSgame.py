# Import the random package so that we can generate random numbers
from random import randint

# choices is an array ==> a containter that can hold multiple items.
# arrays are 0-based ==> the first item is 0, second is 1, etc.
# delcaration of variables!
choices = ["Rock", "Paper", "Scissors"]
player = False
userLives = 3
computerLives = 3
userScore = 0
loop = False
# loop instead of player so that the loop is continuous until player breaks
while loop is False:
    print("===============================================")
    print("Welcome to Rock Paper Scissors!")
    print("You have", userLives, "/3 lives")
    print("The computer has", computerLives, "/3 lives!")
    print("===============================================")

    # make the computer choose a weapon from the choices array at random
    computer_choice = choices[randint(0, 2)]
    # print the choice in the terminal window
    print("Computer chooses: ", computer_choice)
    # give user options to pick
    print("choose your weapon!")
    player = input("Rock, Paper, or Scissors?\n Type 'Quit' to exit\n")
    print(player, "\n")
    # if statements for game; tie
    if player == computer_choice:
        print("Tie! You live to shoot another day.")
    # if statement for user picking rock
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You Lose!", computer_choice, "covers", player)
            userLives = (userLives - 1)
            print("You have", userLives, "lives left")
        else:
            print("You win!", player, "smashes", computer_choice)
            userScore = (userScore + 1)
            print("Your score is", userScore)
            computerLives = (computerLives - 1)
    # if statements for user choosing paper
    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You Lose!", computer_choice, "cuts", player)
            userLives = (userLives - 1)
            print("You have", userLives, "lives left")
        else:
            print("You win!", player, "covers", computer_choice)
            userScore = (userScore + 1)
            print("Your score is", userScore)
            computerLives = (computerLives - 1)
    # if statements for user choosing scissots
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You Lose!", computer_choice, "smashes", player)
            userLives = (userLives - 1)
            print("You have", userLives, "lives left")
        else:
            print("You win!", player, "cuts", computer_choice)
            userScore = (userScore + 1)
            print("Your score is", userScore)
            computerLives = (computerLives - 1)
    elif player == "Quit":
        exit()
    else:
        print("Check your spelling.. Not a valid choice.\n")

# for when the user loses all lives
    if userLives == 0:
        print("You have lost all your lives!")
        print("Your final score was ", userScore)
        # Prompt to play again or quit
        choice = input("Play again? Type 'Yes' to replay, 'Quit' to exit.")
        # variable resets or exit
        if choice == "Yes" or choice == "yes":
            userLives = 3
            userScore = 0
            computer_choice = 3
        elif choice == "Quit" or choice == "quit":
            exit()
# for when the computer loses all lives
    if computerLives == 0:
        print("You have won! Computer lost all lives!")
        print("Your final score was ", userScore)
        # Prompt to play again or quit
        choice = input("Play again? Type 'Yes' to replay, 'Quit' to exit.")
        # variable resets or exit
        if choice == "Yes" or choice == "yes":
            userLives = 3
            userScore = 0
            computerLives = 3
        elif choice == "Quit" or choice == "quit":
            exit()
