# Import the random package so that we can generate random numbers
from random import randint

#choices is an array ==> a containter that can hold multiple itemrs. 
#arrays are 0-based ==> the first item is 0, second is 1, etc.
#delcaration of variables!
choices = ["Rock","Paper","Scissors"]

#make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)] 

#print the choice in the terminal window
print("Computer chooses: ", computer_choice)

#give  