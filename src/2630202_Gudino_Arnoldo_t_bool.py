
"""
HANDLING NUMBERS AND BOOLEANS IN PYTHON

Name: Arnoldo René Gudiño Ponce
Student ID: 2630202
Group: MEC-01
"""

"""
SUMMARY

In Python, int is used for whole numbers and float for decimal numbers.
Boolean values can be True or False.
Comparisons help the program check different conditions.
Arithmetic operators are used to do calculations.
Logical operators like and and or combine conditions.
It is important to check the data entered by the user.
We should avoid dividing by zero because it causes an error.
This activity includes six problems using numbers and booleans.
"""

"""
GOOD PRACTICES

Use int for whole numbers and float for decimal numbers.
Check the input before doing calculations.
Use variable names that are easy to understand.
Save results in variables to make calculations clearer.
Boolean values help the program make decisions.
"""


"""
PROBLEM 1: TEMPERATURE CONVERTER

Description:
Converts Celsius to Fahrenheit and Kelvin.
It also checks if the temperature is high.

Inputs:
Temperature in Celsius.

Outputs:
Fahrenheit, Kelvin, and High temperature.

Validations:
The input must be a number.
The temperature cannot be below -273.15 Celsius.

Test cases:
1. Normal: 25 -> Fahrenheit: 77.0, Kelvin: 298.15,
   High temperature: False
2. Border: -273.15 -> Fahrenheit: -459.67, Kelvin: 0.0,
   High temperature: False
3. Error: abc -> Error: invalid input
"""

print("\nPROBLEM 1: TEMPERATURE CONVERTER")

while True:
    try:
        temp_c = float(input("Enter temperature in Celsius: "))

        if temp_c < -273.15:
            print("Error: invalid input")
        else:
            break

    except ValueError:
        print("Error: invalid input")

temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
is_high_temperature = temp_c >= 30.0

print("Fahrenheit:", temp_f)
print("Kelvin:", temp_k)
print("High temperature:", is_high_temperature)


"""
PROBLEM 2: WORK HOURS AND OVERTIME

Description:
Calculates the weekly pay of a worker.
Hours over 40 are paid at 150% of the normal rate.

Inputs:
Hours worked and hourly rate.

Outputs:
Regular pay, overtime pay, total pay, and Has overtime.

Validations:
Hours must be zero or greater.
Hourly rate must be greater than zero.

Test cases:
1. Normal: 35 hours, rate 100 -> Regular pay: 3500,
   Overtime pay: 0, Total pay: 3500, Has overtime: False
2. Border: 40 hours, rate 100 -> Regular pay: 4000,
   Overtime pay: 0, Total pay: 4000, Has overtime: False
3. Error: hours -5, rate 100 -> Error: invalid input
"""

print("\nPROBLEM 2: WORK HOURS AND OVERTIME")

while True:
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
        else:
            break

    except ValueError:
        print("Error: invalid input")

regular_hours = min(hours_worked, 40)
overtime_hours = max(hours_worked - 40, 0)

regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay

has_overtime = hours_worked > 40

print("Regular pay:", regular_pay)
print("Overtime pay:", overtime_pay)
print("Total pay:", total_pay)
print("Has overtime:", has_overtime)


"""
PROBLEM 3: DISCOUNT

Description:
Checks if a customer can get a discount.
Students, seniors, and customers who spend at least 1000
get a 10% discount.

Inputs:
Purchase total, student answer, and senior answer.

Outputs:
Discount eligible and final total.

Validations:
The purchase cannot be negative.
The answers must be YES or NO.

Test cases:
1. Normal: total 500, student YES, senior NO ->
   Discount eligible: True, Final total: 450.0
2. Border: total 1000, student NO, senior NO ->
   Discount eligible: True, Final total: 900.0
3. Error: total -20 -> Error: invalid input
"""

print("\nPROBLEM 3: DISCOUNT")

while True:
    try:
        purchase_total = float(input("Enter purchase total: "))

        if purchase_total < 0:
            print("Error: invalid input")
        else:
            break

    except ValueError:
        print("Error: invalid input")

while True:
    student_text = input("Are you a student? (YES/NO): ").strip().upper()

    if student_text == "YES" or student_text == "NO":
        is_student = student_text == "YES"
        break
    else:
        print("Error: invalid input")

while True:
    senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

    if senior_text == "YES" or senior_text == "NO":
        is_senior = senior_text == "YES"
        break
    else:
        print("Error: invalid input")

discount_eligible = is_student or is_senior or purchase_total >= 1000

if discount_eligible:
    final_total = purchase_total * 0.9
else:
    final_total = purchase_total

print("Discount eligible:", discount_eligible)
print("Final total:", final_total)


"""
PROBLEM 4: THREE INTEGERS

Description:
Asks for three integers and calculates their sum,
average, maximum, and minimum.
It also checks if all three numbers are even.

Inputs:
Three integers.

Outputs:
Sum, Average, Max, Min, and All even.

Validations:
The inputs must be integers.
Negative numbers are allowed.

Test cases:
1. Normal: 2, 4, 6 -> Sum: 12, Average: 4.0,
   Max: 6, Min: 2, All even: True
2. Border: 0, 0, 0 -> Sum: 0, Average: 0.0,
   Max: 0, Min: 0, All even: True
3. Error: n1 = 2, n2 = abc, n3 = 6 ->
   Error: invalid input
"""

print("\nPROBLEM 4: THREE INTEGERS")

while True:
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))
        break

    except ValueError:
        print("Error: invalid input")

sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)

all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0

print("Sum:", sum_value)
print("Average:", average_value)
print("Max:", max_value)
print("Min:", min_value)
print("All even:", all_even)


"""
PROBLEM 5: LOAN ELIGIBILITY

Description:
Checks if a person meets the conditions for a loan.
It uses income, debt, and credit score.

Inputs:
Monthly income, monthly debt, and credit score.

Outputs:
Debt ratio and Eligible.

Validations:
Income must be greater than zero.
Debt and credit score cannot be negative.

Test cases:
1. Normal: income 10000, debt 2000, score 700 ->
   Debt ratio: 0.2, Eligible: True
2. Border: income 8000, debt 3200, score 650 ->
   Debt ratio: 0.4, Eligible: True
3. Error: income 0, debt 100, score 700 ->
   Error: invalid input
"""

print("\nPROBLEM 5: LOAN ELIGIBILITY")

while True:
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt: "))
        credit_score = int(input("Enter credit score: "))

        if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
            print("Error: invalid input")
        else:
            break

    except ValueError:
        print("Error: invalid input")

debt_ratio = monthly_debt / monthly_income

eligible = (
    monthly_income >= 8000
    and debt_ratio <= 0.4
    and credit_score >= 650
)

print("Debt ratio:", debt_ratio)
print("Eligible:", eligible)


"""
PROBLEM 6: BODY MASS INDEX

Description:
Calculates BMI using weight and height.
It checks if the person is underweight, normal, or overweight.

Inputs:
Weight in kilograms and height in meters.

Outputs:
BMI, Underweight, Normal, and Overweight.

Validations:
Weight and height must be greater than zero.

Test cases:
1. Normal: weight 70, height 1.75 -> BMI: 22.86,
   Underweight: False, Normal: True, Overweight: False
2. Border: weight 76.5625, height 1.75 -> BMI: 25.0,
   Underweight: False, Normal: False, Overweight: True
3. Error: weight 0, height 1.75 -> Error: invalid input
"""

print("\nPROBLEM 6: BODY MASS INDEX")

while True:
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
        else:
            break

    except ValueError:
        print("Error: invalid input")

bmi = weight_kg / (height_m * height_m)

is_underweight = bmi < 18.5
is_normal = bmi >= 18.5 and bmi < 25
is_overweight = bmi >= 25

print("BMI:", round(bmi, 2))
print("Underweight:", is_underweight)
print("Normal:", is_normal)
print("Overweight:", is_overweight)


"""
CONCLUSIONS

I learned that int and float are used for different kinds of numbers.
Comparisons help the program check if a condition is true or false.
It is important to check the data before doing calculations.
Division by zero must be avoided to prevent errors.
The and operator checks if all conditions are true.
The or operator is useful when at least one condition can be true.
These concepts can be used in programs for payments, discounts,
and loan calculations.
"""

"""
REFERENCES

1. Python Documentation - Built-in Types
   https://docs.python.org/3/library/stdtypes.html

2. Python Documentation - Built-in Functions
   https://docs.python.org/3/library/functions.html

3. Python Documentation - Errors and Exceptions
   https://docs.python.org/3/tutorial/errors.html

4. W3Schools - Python Numbers
   https://www.w3schools.com/python/python_numbers.asp

5. W3Schools - Python Booleans
   https://www.w3schools.com/python/python_booleans.asp
"""
