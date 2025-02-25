# Daniel Njaka
# 2/25/25
# P2LAB2
# Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

# get keys from dictionary
cars_keys = cars.keys()

print(cars_keys)

print (*cars_keys, sep = ", ")

# get a car from user
car_name = input("Enter a car: ")

# get mpg for given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

# get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

# calculate
gallons_needed = miles_driven/car_mpg

# display results
print (f"{gallons_needed} gallon(s) of gas are needed to drive the {car_mpg} {miles_driven} miles")
