# Daniel Njaka
# 2/18/25
# P1HW1
# collecting info from user then processing and displaying results

# exponent calculations
print("----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
answer1 = base ** exponent 

# display answer to user
print(f"{base} raised to the power of {exponent} is {answer1} !!")

# addition and subtraction calculations
print("----Addition and Subtraction----")
addend1 = int(input("Enter a starting integer: "))
addend2 = int(input("Enter an integer to add: "))
subtrahend = int(input("Enter an integer to subtract: "))
answer2 = addend1 + addend2 - subtrahend

# display answer to user
print(f"{addend1} + {addend2} - {subtrahend} is equal to {answer2}")
