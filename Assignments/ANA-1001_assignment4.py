# Author: Maaz Sabah Uddin
# StudentId: A00257491
import random

# QUESTION 01
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 01 >>>>>>>>>>>>>>>>>\n")
str1 = "Orange"
str2 = "Mango"

print('Is str1 and str2 are equivalent? I predict False')
print(f'Unfortunately No, {str1 == str2}')

str1 = "maazsabahuddin@gmail.com"
str2 = "MaazSabahuddin@gmail.com"

print('Is str1 and str2 are equivalent? I predict True')
print(f'Yes, {str1 == str2.lower()}')

num1 = 1540
num2 = 1540

print('Is variables num1 and num2 are equivalent? I predict True')
print(f'Yes, {num1 == num2}')

# Checking Is variables num1 and num2 are not equivalent
print('Is variables num1 and num2 are not equivalent? I predict False')
print(f'{num1 != num2}')

num3 = 10
num4 = 20

# Checking Is num4 greater than num3?
print('Is num4 greater than num3? I predict True')
print(f'{num4 > num3}')

# Checking Is num4 greater than or equal to num3?
print('Is num4 greater than or equal to num3? I predict True')
print(f'{num4 >= num3}')

# Checking aIs num4 less than num3?
print('Is num4 less than num3? I predict False')
print(f'{num4 < num3}')

# Checking Is num4 less than or equal to num3?
print('Is num4 less than or equal to num3? I predict False')
print(f'{num4 <= num3}')

# Checking conditions for num3 and num4
if num3 < num4 and num1 == num2:
    print("YES that's True num3 is less than num4 and num1 is equal to num2")

# Checking all the conditional statements
if num3 < num4 or num1 == 0:
    print("YES that's True num3 is less than num4 but num1 is not equal to 0")

fruits = ["Orange", "Mango", "Banana", "Apple"]
print("Is Mango fruit is in the list? I predict True")
print(f"{'Mango' in fruits}")

print("Is Watermelon fruit is in the list? I predict False")
print(f"{'Watermelon' in fruits}")

# QUESTION 02
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 02 >>>>>>>>>>>>>>>>>\n")
# Printing options to user
print("We are now playing a game Paper, Rock, Scissor, Maaz Sabah Uddin")
print("Choose one of the options!")
print("1) Paper")
print("2) Rock")
print("3) Scissor")
print("4) Maaz Sabah Uddin")

user_input = int(input("Please enter your choice: "))
while user_input < 0 or user_input > 4:
    print("You have entered invalid choice of character. Please try again!")
    user_input = int(input("Please enter your choice again: "))

computer_input = random.randint(1, 4)

if user_input == computer_input:
    print(f"Tied! Both players selected paper.")
elif user_input == 2:
    if computer_input == 3:
        print("You win! Rock smashes scissors.")
    else:
        print("You lose! Paper covers rock.")
elif user_input == 1:
    if computer_input == 2:
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cuts paper.")
elif user_input == 3:
    if computer_input == 1:
        print("You win! Scissors cuts paper.")
    else:
        print("You lose! Rock smashes scissors.")


# Question 3
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight/(height/100)**2

if bmi < 18.5:
    print(f"Your BMI is {bmi}. Classification: 'Underweight'. "
          f"Risk of developing health problems Increased")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}. Classification: 'Normal Weight'. "
          f"Risk of developing health problems Least")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}. Classification: 'Overweight'. "
          f"Risk of developing health problems Increased")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}. Classification: 'Obese Class II'. "
          f"Risk of developing health problems High")
elif 35 <= bmi < 40:
    print(f"Your BMI is {bmi}. Classification: 'Obese Class II'. "
          f"Risk of developing health problems Very High")
elif bmi >= 40:
    print(f"Your BMI is {bmi}. Classification: 'Obese Class III'. "
          f"Risk of developing health problems Extremely high")

# Question 4
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 04 >>>>>>>>>>>>>>>>>\n")
# List of pizza customers
pizza_customers = ["Maaz", "Shahrukh", "Shamekh", "Zeerak", "Abdullah"]
# List of pizza candidates
pizza_candidates = ["Ali", "Maaz", "Owais", "Abdullah", "Mohib"]

# Looping through pizza candidates
for candidate in pizza_candidates:
    if candidate in pizza_customers or candidate.lower() in pizza_customers:
        print(f"Hi {candidate}. You're already a member of Pizza store.")
    else:
        print(f"Hi {candidate}. You're not a member of Pizza store. You are able to join us and there are a lot "
              f"of benefits.")

# Question 5
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 05 >>>>>>>>>>>>>>>>>\n")
numbers = list(range(1, 10))
for num in numbers:
    # All conditional statements
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')


# Question 6
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 06 >>>>>>>>>>>>>>>>>\n")
computer_player_num = random.randint(1, 10)
player = 7

print(f"Computer Player {computer_player_num}")
print(f"Player {player}")

# Conditional statements
if player == computer_player_num:
    # If both are equal
    print("Both numbers are equal")
elif player > computer_player_num:
    # If player is greater than random selected value
    print("Player Number is greater")
else:
    # Else this will print
    print("Player Number is less")


# Question 7
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 07 >>>>>>>>>>>>>>>>>\n")
one_die = random.randint(1, 6)
# A die list with random number from 1 to 6
die = [one_die]

# A dice list with random number from 1 to 6
two_die = random.randint(1, 6)
dice = list()
# Inserting and appending values to dice list
dice.insert(0, two_die)
dice.append(one_die)

print(f"Die {die}")
print(f"Dice {dice}")


# Question 8
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 08 >>>>>>>>>>>>>>>>>\n")
temperature_khi = 29
# Formula to convert in fahrenheit and kelvin
print(f"The weather in Karachi is {temperature_khi}C which is {(temperature_khi*9/5)+32}F "
      f"and {temperature_khi+273.15}K")

# Question 9
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 09 >>>>>>>>>>>>>>>>>\n")
# Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The final block lets you execute code, regardless of the result of the try- and except blocks.

# This is basically used for exception handling. Whenever there is a chance for error you can use try except block so
# that your program won't crash

try:
    x = "a"
    # Converting string to integer it will through an error because x is a string variable.
    y = int(x)
except ValueError as e:
    # Since the try block raises an error, the except block will be executed.
    # Without the try block, the program will crash and raise an error:
    print("This is failed case of catching exceptions block in python. The below error corresponds"
          "Converting string to integer it will through an error because x is a string variable.")
    print(f"\nError: {e}")


# Question 10
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 10 >>>>>>>>>>>>>>>>>\n")
card_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'spades', 'hearts']

# Selecting random value of card numbers and suits
print(f"You got {random.choice(card_numbers)} of {random.choice(suits)}")
