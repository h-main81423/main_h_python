print ("Rules that govern the state of water")

# set up a variable to hold the temperature we input
current_temp = False

while current_temp is False:
    current_temp = input("Enter a temperature:\n")
    # see what you input
    print("you input:", current_temp)

    # if water is below odr freezing, solid.
    if (int(current_temp) < 0 or (int(current_temp) == 0)):
        print("water is solid. It is at or below freezing")
        current_temp = False
    # else check another condition, oif it is not freezing, is it boiling?
    elif (int(current_temp) < 100):
        print("water is a liquid, because it is above freezing and below boil")
        current_temp = False

    elif (int(current_temp) > 100):
        print("Water is a gas, because it's pretty damn hot.")
        current_temp = False
