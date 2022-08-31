# Author: Maaz Sabah Uddin
# StudentId: A00257491
import random


# Q1: Think about the city you were born. Make a Python list of some of the interesting things
# to see.  Use your list to print a series of statements about these items,
# such as "Paris is wonderful in the spring because everyone is eating crepes".
# Print one statement for each item in your list using a fstring. Print the statements
# using the index position counting from the beginning, the middle, and end of the list.

print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 01 STARTED >>>>>>>>>>>>>>>>>>>")
city_interesting_things = ["Karachi is a beautiful place",
                           "In Karachi there is a place DoDarya",
                           "Sports club is a place where everybody comes and play their "
                           "favorite sports.",
                           "One of the finest place at Bahria Town Karachi",
                           "In Karachi there are different number of clubs, in those"]

# 0 index mean first value of the list
print(f"{city_interesting_things[0]} because it's soo charming")

# 1 index mean second value of the list
print(f"{city_interesting_things[1]} which is a Coastal district with sunset viewpoints "
      f"terrace restaurants overlooking the water.")

# 2 index mean second value of the list
print(f"{city_interesting_things[2]} because it is amazing and the ticket is $4.1 for adults "
      f"while $2.3 for children. Amazing place for children. One can have a free buggy ride "
      f"with a driver as a guide who is able to elaborate sight seeing and animal species.")

# -1 index mean last value of the list (means last index)
print(f"{city_interesting_things[-1]} Arena club is best for friends gathering this is the only "
      f"one club in area have great bowling playing games")


# Question 02:
print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 02 STARTED >>>>>>>>>>>>>>>>>>>")
print(">>>>> STEP 1 >>>>>\n")
friends_mission = ["Maaz", "Azka", "Shahrukh", "Zeerak", "Shamekh"]
print(f"{friends_mission[0]} we're going on a mission to save humanity. Be ready and "
      f"report me.")
# -4 index mean fourth last value of the list (means fourth last index)
print(f"{friends_mission[-4]} we're going on a mission to save humanity. Be ready and "
      f"report me.")
# -3 index mean third last value of the list (means third last index)
print(f"{friends_mission[-3]} we're going on a mission to save humanity. Be ready and "
      f"report me.")
# -2 index mean second last value of the list (means second last index)
print(f"{friends_mission[-2]} we're going on a mission to save humanity. Be ready and "
      f"report me.")
# -1 index mean last value of the list (means last index)
print(f"{friends_mission[-1]} we're going on a mission to save humanity. Be ready and "
      f"report me.")
# Using len function to print the number of friends going on a mission
print(f"We are {len(friends_mission)} friends who are going on a mission to save humanity.")

print("\n>>>>> STEP 2 >>>>>\n")
print(f"We are unable to go to a mission because of you {friends_mission[3]}. We need someone"
      f"else to move further")
friends_mission[3] = "Abdullah"
print(f"{friends_mission} guys we have a new volunteer who is willing to go with us.")
print(f"We are {len(friends_mission)} friends who are going on a mission to save humanity.")

print("\n>>>>> STEP 3 >>>>>\n")
friends_mission.insert(0, "Celebrity A")
middle = len(friends_mission) // 2
friends_mission.insert(middle, "Celebrity B")
friends_mission.append("Celebrity C")
print(friends_mission)
print(f"We are {len(friends_mission)} peoples who are going on a mission to save humanity.")

print("\n>>>>> STEP 4 >>>>>\n")
print(f"Hello guys {friends_mission}, among all of us only two of us will be able to attend "
      f"the mission because there's no room for the third person")

# They are not going for mission
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")
print(f"{friends_mission.pop()} sorry mate, you will not be able to attend the mission.")

# Below both of them are going on a mission
print(f"{friends_mission[0]} you're going on a mission to save the humanity")
print(f"{friends_mission[1]} you're going on a mission to save the humanity")
print(f"We are {len(friends_mission)} peoples who are going on a mission to save humanity.")


print("\n>>>>> STEP 5 >>>>>\n")
del friends_mission
# We cannot use list after deleting it, so printing will not have effect,
# and it will through NameError
# print(friends_mission)
# print(f"We are {len(friends_mission)} peoples who are going on a mission to save humanity.")


# Question 03:
print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 03 STARTED >>>>>>>>>>>>>>>>>>>")
football_places = ["Canada", "Pakistan", "Brazil", "Singapore", "Bangladesh"]
print(football_places)

football_places_copy = football_places.copy()
# Print sorted list without modifying the original list
# I just made a copy of original and sort it and print the list
football_places_copy = sorted(football_places_copy)
print(football_places_copy)

# Reversing the list in alphabetical order
football_places_copy.reverse()
print(football_places_copy)

# Reversing the list again to make it in original form
football_places_copy.reverse()
print(football_places_copy)

# sorting original list
football_places.sort()
print(football_places)

# sorting original list again
football_places.sort(reverse=True)
print(football_places)


# Question 04:
print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 04 STARTED >>>>>>>>>>>>>>>>>>>")
places = ["Minar-e-Pakistan", "Sports Club", "Cambrian College"]
colors = ["Black", "Orange", "White", "Green"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foods = ["Biryani", "Daal Chawal", "Tikka", "Burgers"]
cars = ["Toyota", "Honda", "Nissan"]

# Printing data related to different lists
print(f"{random.choice(places).title()} is my favorite place.")
print(f"{random.choice(colors).title()} is one the most darkest color. Lets make it light.")
print(f"{random.choice(numbers)} is chosen randomly.")
print(f"{random.choice(foods).title()} is a dish in Pakistan and one of the most common "
      f"in my city Karachi.")
print(f"I own {random.choice(cars).title()} brand car in my late 20's.")


# Question 05:
print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 05 STARTED >>>>>>>>>>>>>>>>>>>")
student_number = ["A", 0, 0, 2, 5, 7, 4, 9, 1]
# Adding digits all over
add_digits = student_number[1] + student_number[2] + student_number[3] + student_number[4] + \
             student_number[5] + student_number[6] + student_number[-2] + student_number[-1]
print(f"The sum of all the digits in my student number is {add_digits}")

# Converting into string and print it
print(f"{str(student_number[1])}{str(student_number[2])}{str(student_number[3])}"
      f"{str(student_number[4])}{str(student_number[5])}{str(student_number[6])}"
      f"{str(student_number[7])}{str(student_number[-1])}")


# Question 06:
print("\n\n>>>>>>>>>>>>>>>>>>> QUESTION 06 STARTED >>>>>>>>>>>>>>>>>>>")
meals = [["egg", "tea", "cake rusk"],
         ["biryani", "burgers", "shawarma"],
         ["tikka", "Karahi", "Beef Kabab"]]

# Printing first sublist data
print(f"First item of first sublist {meals[0][0]}")
print(f"Last item of first sublist {meals[0][-1]}")

# Printing second sublist data
print(f"First item of second sublist {meals[1][0]}")
print(f"Last item of second sublist {meals[1][-1]}")

# Printing third sublist data
print(f"First item of third sublist {meals[2][0]}")
print(f"Last item of third sublist {meals[2][-1]}")
