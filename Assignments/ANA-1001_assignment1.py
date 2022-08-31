# Author: Maaz Sabah Uddin
# StudentId: A00257491

# Question 1:
# Describe four programs you would like to create using full sentences.
# Remember to comment your answers so your code runs.

# 1- A program that take user input their weight and height and results user BMI.
# 2- Build a program that works as a calculator until user enter '@'.
# 3- Get any number and print its table.
# 4- Create balance sheet with debit/credit statement.

# Question 2:
# First store the name of a city (the value) in a variable, and then print the name.
# Repeat this process with two other city names but use the same variable name.
# Format the output using .title() and .upper()

# Declared a variable 'city' and assign a value "Karachi" to it.
city = "Karachi"
print(city)
# Declared a variable 'city' and assign a value "lahore" to it.
city = "lahore"
print(city.title())
# Declared a variable 'city' and assign a value "Multan" to it.
city = "Multan"
print(city.upper())

# Question 3:
# Store your name in a variable and print out your name within a sentence using an f string.
# Do this three times, modifying your name to print out in uppercase, lowercase and title case.

# Declared a variable 'name' and assign a value "lahore" to it.
name = "Maaz Sabah Uddin"
print(f"My name is: {name}")
# Applied .upper function to string type variable
print(f"My name is: {name.upper()}")
# Applied .lower function to string type variable
print(f"My name is: {name.lower()}")
# Applied .title function to string type variable
print(f"My name is: {name.title()}")


# Question 4:
# Use a variable to represent the name of a Canadian food. You are then going to print this variable four times.
# Before you do, print the Canadian food out  and include some white space characters at the beginning and end
# and use "\t" and "\n" a least once. Then print the food once, so the white space is displayed.
# Remember, you may not be able to see the white space on the right hand side. Following the food name print,
# print the name out three times, once using each of the three stripping functions lstrip(), rstrip(), and strip().

canadian_food = "\tPasta\t\n"
print(f"{canadian_food}")
# Applied .lstrip function to string type variable. It will remove the spaces from left
print(canadian_food.lstrip())
# Applied .rstrip function to string type variable. It will remove the spaces from right
print(canadian_food.rstrip())
# Applied .strip function to string type variable. It will remove the spaces from left and right
print(canadian_food.strip())


# Question 5:
# Write four operations (addition, subtraction, multiplication, and division) to equal 2022.
# Then store each in a variable and print a message explaining your results.
# Substitute 2022 for your variable name to display the string. (for example, print would show:
# Multiplying 202.2 ten times equals 2022). Print two of them using an f string (f) and two using a join (+ or ,).

# Addition
# Declared and initialized two variables and add them
n1 = 1011
n2 = 1011
print(f"Sum of {n1} and {n2} is: {n1+n2}")

# Subtraction
# Declared and initialized two variables and subtract them
n1 = 3033
n2 = 1011
print(f"Subtracting {n2} from {n1} is: {n1-n2}")

# Multiplication
_mult = int(20.22 * 100)  # Converting into int because the answer was in float data type
print("Multiplying 20.22 one hundred times equals: " + str(_mult))

# Division
_div = 428664 // 212  # Double slash to round off the value.
print("Diving 212 by 428664 is: ", str(_div))


# Question 6:
# A dog runs from one side of a park to the other. The park is 80.0 meters across.
# The dog takes 16.0 seconds to cross the park. What is the speed of the dog?
# Answer: The distance the dog travels and the time it takes are given.
# The speed of the dog is 5.0 meters per second. The dog’s speed can be found with the formula:
# s = 5.0 m/s
# Write this formula as a calculation in Python (create variables for speed, distance, and time)
# and print out the resulting solution in a sentence using an fstring.

# Formula we are going to use is 'distance = speed (displacement) x time'
# According to the given data distance is in metres and time is in seconds

# Data
distance = 80
time = 16

# Applying formula
speed = distance / time
print(f"The speed of the dog is {speed} meters per second")
