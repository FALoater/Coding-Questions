# create a program that asks the user for a letter
# and then converts that letter to uppercase or lowercase, depending on the letter
# also validate input, so that if the user doesn't enter a letter it will not run
# also make sure that the user only enters 1 letter
# for reference, "A" is 65 in ASCII and "a" is 97 in ASCII

from typing import final


invalid = True
while invalid:
    userInput = input("Enter one letter:\n")
    letterToAscii = ord(userInput) # conv to ASCII

    if(len(userInput) != 1):
        print("You have not matched the required length.") # if length of input is not 1
    else:
        
        if((letterToAscii < 65) or (letterToAscii > 90) and (letterToAscii < 97) or (letterToAscii > 122)): # checks if the input is a letter
            print("You have not entered a letter.")
        else:
            invalid = False

#now check the case
caseOfInput = ""

if(userInput == userInput.lower()):# checks if lowercase.
    caseOfInput = "lowercase"
else: # if not then the letter is uppercase
    caseOfInput = "uppercase"

if(caseOfInput == "lowercase"):
    letterToAscii -= 32 # minus 32 to convert to uppercase
    finalLetter = chr(letterToAscii)
else:
    letterToAscii += 32
    finalLetter = chr(letterToAscii)

print(f"Your letter converted is {finalLetter}.")
