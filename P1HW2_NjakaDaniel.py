# Daniel Njaka
# 2/18/25
# P1HW2
# calculating and displaying travel expenses

# tell user what program does
print("This program calculates and displays travel expenses")

# calculation inputs

budget = int(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

remain = budget - gas - accomodation - food

# display travel expenses

print("----Travel Expenses----")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {accomodation}")
print(f"Food: {food}")
print()
print(f"Remaining balance: {remain}")