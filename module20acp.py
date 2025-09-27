# Square it Out
print("Activity: Square it Out")
nums = [1, 2, 3, 4, 5]
squared_nums = [x**2 for x in nums]
print(f"Original numbers: {nums}")
print(f"Squared numbers: {squared_nums}")
print("\n" + "-"*40 + "\n")



# Tuple Product
print("Activity: Tuple Product")
t = (2, 3, 4)
product = 1
for val in t:
    product *= val
print(f"Tuple: {t}")
print(f"Product of tuple elements: {product}")
print("\n" + "-"*40 + "\n")


# Tuples
print("Activity: Tuples")
sample_tuple = (1, 'hello', 3.14, True)
print(f"Sample tuple: {sample_tuple}")
print(f"First element: {sample_tuple[0]}")
print(f"Tuple slicing (1:3): {sample_tuple[1:3]}")
print("\n" + "-"*40 + "\n")


# Check the frequency
print("Activity: Check the frequency")
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(f"Words list: {words}")
print(f"Frequencies: {freq}")
print("\n" + "-"*40 + "\n")




# Set Symmetric Difference
print("Activity: Set Symmetric Difference")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
sym_diff = set_a.symmetric_difference(set_b)
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Symmetric difference: {sym_diff}")
print("\n" + "-"*40 + "\n")



# List Comprehension Practise
print("Activity: List Comprehension Practise")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares of even numbers between 0-9: {even_squares}")
print("\n" + "-"*40 + "\n")



# Random Password Generator
print("Activity: Random Password Generator")
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(f"Random password: {generate_password()}")
print("\n" + "-"*40 + "\n")

