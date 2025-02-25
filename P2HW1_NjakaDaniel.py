# Daniel Njaka
# 2/25/25
# P2HW1
# calculating and displaying travel expenses but fancy this time

# tell user what program does
print("This program calculates and displays travel expenses")

# calculation inputs

budget = float(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remain = budget - gas - accomodation - food

# display travel expenses

print("\n------------Travel Expenses------------")
print(f"Location:            {destination}")
print(f"Initial Budget:      ${budget:.2f}")
print(f"Fuel:                ${gas:.2f}")
print(f"Accomodation:        ${accomodation:.2f}")
print(f"Food:                ${food:.2f}")
print("----------------------------------------")
print(f"Remaining balance:   ${remain:.2f}")