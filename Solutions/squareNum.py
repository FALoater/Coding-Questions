#create a program that asks the user for a number, validate that it is an integer, and then print the square of it
variableInvalid = True
while variableInvalid:
    try:
        userInput = int(input("Enter a number:\n"))
        variableInvalid = False
    except:
        print("Invalid number")

squareOfInput = userInput ** 2
print(f"The square of your number entered is: {squareOfInput}.")