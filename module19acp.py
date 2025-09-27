# ACP: Circumference
# Lesson: Function
import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle is: {calculate_circumference(radius)}")


# ACP: Shutdown
# Lesson: Arguments
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# ACP: Due Amount
# Lesson: Keywords
def calculate_due_amount(total_amount, paid_amount):
    due_amount = total_amount - paid_amount
    return due_amount

total_amount = float(input("Enter the total amount: "))
paid_amount = float(input("Enter the paid amount: "))
print(f"The due amount is: {calculate_due_amount(total_amount, paid_amount)}")


# ACP: Due Amount
# Lesson: Keywords

def calculate_due_amount(total_amount, paid_amount):
    due_amount = total_amount - paid_amount
    return due_amount

# Using a while loop to repeatedly ask for input until valid data is entered

while True:
    try:
        total_amount = float(input("Enter the total amount: "))
        paid_amount = float(input("Enter the paid amount: "))

        if total_amount < 0 or paid_amount < 0:
            print("Amounts cannot be negative! Try again.")
            continue 

        if total_amount == 0:
            print("Total amount cannot be zero. Exiting...")
            break  

        print(f"The due amount is: {calculate_due_amount(total_amount, paid_amount)}")
        break  

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        pass 


# ACP: Age Counter
# Lesson: Exception Handling
def divide_numbers(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"An error occurred: {e}"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"The result of division is: {divide_numbers(num1, num2)}")


# ACP: Trigonometric Value
# Lesson: Random and Math Module
import random
import math

def generate_random_number():
    return random.randint(1, 100)

def calculate_square_root(number):
    return math.sqrt(number)

random_number = generate_random_number()
print(f"Random number generated: {random_number}")
print(f"Square root of {random_number}: {calculate_square_root(random_number)}")


# ACP: Months
# Lesson: Date, Time, and Calendar
import calendar
from datetime import datetime

def display_current_date_and_time():
    now = datetime.now()
    print(f"Current Date and Time: {now}")

def display_current_month():
    current_month = calendar.month_name[datetime.now().month]
    print(f"Current Month: {current_month}")

month_number = int(input("Enter a month number (1-12): "))
print(f"The month is: {calendar.month_name[month_number]}")

display_current_date_and_time()
display_current_month()
