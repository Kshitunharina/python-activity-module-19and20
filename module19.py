# Activity: Well Wishes
def well_wishes():
    print("hello")
    print("how are you?")
 
well_wishes()


# Activity: Weather Condition
def weather_condition():
    spring = "autumn"
    autumn = spring
    print('The weather is pleasant in:', spring)
    print('The weather is same in', autumn)

weather_condition()


# Activity: Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Display operation menu
print("Welcome to the Simple Calculator")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user choice
choice = input("Enter your choice (1/2/3/4): ")

# Validate and take number input
if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid choice. Please select a valid operation.")


# Activity: Perimeter
def perimeter_rectangle(length, width):
    return 2 * (length + width)

# perimeter
l = float(input("Enter length: "))
w = float(input("Enter width: "))
print("Perimeter of rectangle is:", perimeter_rectangle(l, w))


# Activity: Number Conversion
def convert_number(number):
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)

    print("\nHere are the converted values:")
    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)

# Ask the user to enter a number
user_input = input("Enter a whole number (in decimal): ")

# Check if the input is a valid number
if user_input.isdigit():
    num = int(user_input)
    convert_number(num)
else:
    print("Oops! Please enter a valid whole number.")


# Activity: Tip The Waiter
def total_calc(bill_amount, tip_perc):
    # Define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# specify only bill_amount
# default value of tip percentage is used
total_calc(150, 20)


# Activity: Cube of the Cube
def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(by_three(9))  
print(by_three(4))


# Activity: Factorial
def factorial(x):
    """This is a recursive function to find the factorial of an integer."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

# Display the docstring
print(factorial.__doc__)

# Display results
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 4:", factorial(4))  # fixed the label
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))


# Activity: Break, Pass, Continue
a = input("Enter a word: ")

# Program to check if 'A' is in the input using break
for i in a:
    if i == 'A':
        print("A is found")
        break
else:
    print("A not found")

# Demonstrating break, pass, and continue in loop
for x in range(10):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)


# Activity: Current Letter
var = 10

while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('\nCurrent variable value:', var)

print("\nGood bye!")


# Activity: Present Number
word = input("Enter a word: ")

print("\nChecking each letter:")

for letter in word:
    if letter == 'a':
        print("Found letter 'a', stopping the loop.")
        break
    elif letter == 'e':
        print("Found letter 'e', skipping this letter.")
        continue
    print("Current letter:", letter)

print("\nLoop ended.")


# Activity: Value Error
numbers = [5, 10, 15, 20, 25, 30]

# Take user input
user_number = int(input("Enter a number to check if it is present: "))

# Flag to track if number found
found = False

# Iterate through the list
for num in numbers:
    if num == user_number:
        print(f"The number {user_number} is present in the list.")
        found = True
        break
else:
    print(f"The number {user_number} is NOT present in the list.")


# Activity: Multiple Exceptions
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
    
except ValueError as ex:
    print("Exception:", ex)


try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by a comma like 1, 2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")


# Activity: Bye Bye
valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("Bye")
            valid = True
            break
        if not valid:
            print("The number is not even. Try again.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Activity: Raise Exception
def check_positive(number):
    if number < 0:
        raise ValueError("Negative number entered! Please enter a positive number.")

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
    print(f"You entered: {num}")
except ValueError as e:
    print("Error:", e)


# Activity: LCM
def calculate_lcm(x, y):
    if x == 0 or y == 0:
        raise ValueError("LCM is not defined for zero.")
    lcm = max(x, y)
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += 1

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    lcm = calculate_lcm(num1, num2)
    print(f"LCM of {num1} and {num2} is {lcm}")
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Unexpected error:", e)


# Activity: Number Game
import random

playing = True
number = str(random.randint(10, 20))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. \n")


# Activity: Rock Paper Scissors
import random

options = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!")
print("Enter your choice (rock, paper, or scissors):")

while True:
    user_choice = input().lower()

    if user_choice not in options:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


# Activity: Mathematical Operations
import math

print('The Floor and Ceiling value of 23.56 are: ' +
      str(math.floor(23.56)) + ', ' + str(math.ceil(23.56)))

x = 10
y = -15

print('The value of x after copying the sign from y is: ' +
      str(math.copysign(x, y)))

print('Absolute value of -96 and 56 are: ' +
      str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56: ' + str(math.gcd(24, 56)))


# Activity: Math with Condition
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
    print(f"Square root of {num} is {math.sqrt(num)}")
elif num < 0:
    print(f"{num} is negative.")
    print(f"Absolute value of {num} is {math.fabs(num)}")
else:
    print("You entered zero.")


# Activity: Is close Math
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if math.isclose(a, b):
    print(f"{a} and {b} are approximately equal.")
else:
    print(f"{a} and {b} are NOT approximately equal.")


# Activity: Current Date and Time
from datetime import date, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\nCurrent Date and time is", now)

print("\nDate components:", today.year, today.month, today.day)


# Activity: Random Date and Time
import random
from datetime import datetime, timedelta

def random_date(start, end):
    delta = end - start
    int_delta = int(delta.total_seconds())
    random_second = random.randint(0, int_delta)
    return start + timedelta(seconds=random_second)

start_date = datetime(2020, 1, 1, 0, 0, 0)
end_date = datetime(2023, 12, 31, 23, 59, 59)

random_datetime = random_date(start_date, end_date)
print("Random date and time generated:", random_datetime)


# Activity: Trip Expenditure
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0

def rental_car_cost(days):
    cost_per_day = 40
    total = cost_per_day * days
    if days > 7:
        total -= 50
    elif days >= 3:
        total -= 20
    return total

def trip_cost(city, days):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)

city = input("Enter your destination city: ")
days = int(input("Enter number of days for your trip: "))

total = trip_cost(city, days)
print(f"Total trip cost for {days} days in {city}: ${total}")


# Activity: First Day of the Month
from datetime import datetime

now = datetime.now()

first_day_of_month = datetime(now.year, now.month, 1, now.hour, now.minute, now.second)

print("First day of this month with current time:", first_day_of_month)


# Activity: Current Time
from datetime import datetime

# Get current date and time
now = datetime.now()

print("Current date and time:", now)
