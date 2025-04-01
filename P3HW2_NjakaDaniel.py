# Daniel Njaka
# 3/16/25
# P3HW2
# Show employee information

# Input values 
employee_name = input("Enter employee's name: ") 
hours_worked = float(input("Enter number of hours worked: ")) 
pay_rate = float(input("Enter employee's pay rate: ")) 
# Calculations 
overtime_hours = max(0, hours_worked - 40) 
regular_hours = min(40, hours_worked) 
overtime_pay = overtime_hours * (pay_rate * 1.5) 
regular_pay = regular_hours * pay_rate 
gross_pay = regular_pay + overtime_pay 
# Output 
print("Employee name:", employee_name) 
print("Hours Worked:", hours_worked)
print("Pay Rate:", pay_rate) 
print("Overtime:", overtime_hours) 
print("Overtime Pay:", overtime_pay) 
print("Regular Pay:", regular_pay) 
print("Gross Pay:", gross_pay)