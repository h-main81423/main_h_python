def greetings():
    print("Hello from the greetings function")


# the greetings function just says hello
# invoke or call the function
greetings()


def greetingsWithArgs(msg="a default message"):
    # print the msg variable
    print("now we're saying", msg, "from another function.")


greetingsWithArgs("eat my fuckin weenie")
greetingsWithArgs("damn dis sucks cock")
greetingsWithArgs()

# returning values from functions can be a very powerful tool


def someMath(num1=2, num2=4):
    return num1 + num2


sum = someMath()
print("We are doing math and getting", sum)

sum = someMath(10, 15)
print("More math and we are getting", sum)
