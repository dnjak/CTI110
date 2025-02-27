# Daniel Njaka
# 2/27/25
# P2HW2
# display grade average from user input using a list

# have user input the grades

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# calculations
grades = [mod1, mod2, mod3, mod4, mod5, mod6]
lowest = min(grades)
highest = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# show results
print("\n--------Results--------")
print(f"Lowest Grade: {lowest}")
print(f"Highest Grade: {highest}")
print(f"Sum of Grades: {sum}")
print(f"Average of Grades: {avg}")
print("-----------------------")