# Getting Started with Lists
empty_list = []
print(empty_list)

numbers = [1, 2, 3, 4, 5]
print(numbers)

triples = [1, 2, 3] * 3
print(triples)

aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList, "\n")


# Word Matching
def match_words(words):
    ctr = 0
    matched_words = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            matched_words.append(word)
    print("List of words with first and last character same:\n", matched_words)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)


# Sum and Average
L = [10, 20, 30, 5, 50, 15]
count = 0
for i in L:
    count += i
avg = count / len(L)
print("Sum =", count)
print("Average =", avg)

L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])


# Zip These Lists
list1 = [10, 20, 30]
list2 = [1, 2, 3]
sum_list = [a + b for a, b in zip(list1, list2)]
print("List 1:", list1)
print("List 2:", list2)
print("Sum of lists:", sum_list)


# Split It
items = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(items) // 2
first_half = items[:mid]
second_half = items[mid:]
print("Original List:", items)
print("First Half:", first_half)
print("Second Half:", second_half)


# Tuples
mixed_tuple = (10, "Hello", 3.14, True)
print("1. Mixed Datatype Tuple:", mixed_tuple)

int_tuple = (1, 2, 3, 4, 5)
print("2. Integer Tuple:", int_tuple)

added_tuple = tuple(x + 9 for x in int_tuple)
print("3. New Tuple after adding 9:", added_tuple)

count_10 = mixed_tuple.count(10)
print("4. Occurrences of 10 in mixed_tuple:", count_10)

sliced_tuple = int_tuple[1:4]
print("5. Sliced Tuple (index 1 to 3):", sliced_tuple)


# Flip Flop
def palind(r):
    s = 0
    e = len(r) - 1
    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

r = (1, 2, 3, 3, 2, 1)
if palind(r):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")


# Weather Prediction
weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0

for i in range(7):
    if weather[i] == 0:
        rainy += 1
    else:
        sunny += 1

if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")


# Tuple Average
numbers = (10, 20, 30, 40, 50)
average = sum(numbers) / len(numbers)
print("Average of tuple elements:", average)


# All About Dictionary
student_data = {
    'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
}

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)


# Get rid of the duplicates
test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("The original dictionary : " + str(test_dict))

K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1
print("Frequency of K is: " + str(res))


# Check the key.
SPCMcountry_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}
print("Country code for India -", SPCMcountry_code.get('India', 'Not Found'))
print("Country code for Japan -", SPCMcountry_code.get('Japan', 'Not Found'))


# Mirroring
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
mirrored_dict = {value: key for key, value in original_dict.items()}
print("Original dictionary:", original_dict)
print("Mirrored dictionary:", mirrored_dict)


# Sets and Arrays
int_set = {10, 20, 30, 40}
print("1. Set with integer elements:", int_set)

mixed_set = {10, "Hello", 3.14, True}
print("2. Set with mixed data types:", mixed_set)

set_with_duplicates = {1, 2, 3, 4, 3, 2}
print("3. Set created from elements with duplicates:", set_with_duplicates)

list_elements = [1, 2, 3, 2]
set_from_list = set(list_elements)
print("4. Set created from list:", set_from_list)

original_list = [0, 1, 3, 4, 5]
temp_set = set(original_list)
first_element = original_list[0]
temp_set.remove(first_element)
print("5. Set after removing first element:", temp_set)


# Set Operations
setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)


# Arrays
import array as arr
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: " + str(array_num))
print("Number of occurrences of the number 3 in the said array: " + str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))


# Frozenset
fset = frozenset([1, 2, 3, 4, 5, 3, 2])
print("Frozen set:", fset)

another_fset = frozenset([4, 5, 6, 7])
print("Intersection:", fset.intersection(another_fset))
print("Union:", fset.union(another_fset))


# Advanced Python Functions
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

nums = [1, 2, 3, 4, 5]

def sq(n):
    return n * n

square = list(map(sq, nums))
print("Square of numbers in list")
print(square)


# Hands on Map
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

zipped_list = list(zip(list1, list2))
print("1. Zipped list:", zipped_list)

zipped_reverse = list(zip(list1, list2[::-1]))
print("2. Zipped with 2nd list reversed:", zipped_reverse)

zipped_dict = dict(zip(list1, list2))
print("3. Zipped into dictionary:", zipped_dict)


# That's the exit
for i in range(10):
    if i == 5:
        print("Exiting the program")
        exit()
    print(i)


# Python Tic Tac Toe
theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

board_keys = list(theBoard.keys())

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    while True:
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")
        move = input()

        if move not in board_keys:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        if count >= 5:
            if (theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ') or \
               (theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ') or \
               (theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ') or \
               (theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ') or \
               (theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ') or \
               (theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ') or \
               (theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ') or \
               (theBoard['9'] == theBoard['5'] == theBoard['1'] != ' '):
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play Again? (y/n): ")
    if restart.lower() == 'y':
        for key in board_keys:
            theBoard[key] = ' '
        game()

if __name__ == "__main__":
    game()


# Guess the Number
import random 
import time

number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")
    global name
    name = input()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 100")
    x = 'even' if number % 2 == 0 else 'odd'
    print(f"\nThis is an {x} number")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)
            if 1 <= guess <= 100:
                guessesTaken += 1
                if guess < number:
                    print("The guess of the number that you have entered is too low")
                elif guess > number:
                    print("The guess of the number that you have entered is too high")
                else:
                    break
                if guessesTaken < 6:
                    time.sleep(.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except:
            print(f"I don't think that {enter} is a number. Sorry")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}')

playagain = "yes"
while playagain.lower() in ("yes", "y"):
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()
