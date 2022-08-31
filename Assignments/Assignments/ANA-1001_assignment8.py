# Author: Maaz Sabah Uddin
# StudentId: A00257491
# Assignment 08
import time
from random import randint


# Question 1
print("\n>>>>>>>>>>>>>>>>> QUESTION 01 & 02 >>>>>>>>>>>>>>>>>\n")
NUMBER_OF_SIDES_SIX = 6
NUMBER_OF_SIDES_TEN = 10
NUMBER_OF_SIDES_TWENTY = 20


class Die:

    def __init__(self, sides=NUMBER_OF_SIDES_SIX):
        self.sides = sides
        self.spins = []

    def roll_die(self):
        toss = randint(1, self.sides)
        self.spins.append(f' {str(toss)} ')

    @staticmethod
    def roll_dice(sides):
        toss1 = randint(1, sides)
        toss2 = randint(1, sides)
        file2 = open("dice.txt", "a")
        file2.write(f"Pair of this toss is: {toss1} and {toss2}\n")
        file2.close()

    def save_to_file(self):
        f = open("die.txt", "a")
        f.write(f"{self.sides} sides die\n")
        f.writelines(self.spins)
        f.write("\n")
        f.close()

    @staticmethod
    def read_from_file(file_name):
        fR = open(file_name, "r")
        print(fR.read())
        fR.close()


# Objects for Question 1
die_obj1 = Die(sides=NUMBER_OF_SIDES_SIX)
for i in range(10):
    die_obj1.roll_die()
die_obj1.save_to_file()

die_obj2 = Die(sides=NUMBER_OF_SIDES_TEN)
for i in range(10):
    die_obj2.roll_die()
die_obj2.save_to_file()

die_obj3 = Die(sides=NUMBER_OF_SIDES_TWENTY)
for i in range(10):
    die_obj3.roll_die()
die_obj3.save_to_file()
Die.read_from_file(file_name="die.txt")

# Object for Question 2
Die.roll_dice(sides=NUMBER_OF_SIDES_TEN)
obj = Die()
obj.read_from_file(file_name="dice.txt")


# Question 3
print("\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")
FILE_NAME_TIME = "time.txt"
TOTAL_INVESTMENT = 1000000

data = None
try:
    fileR = open(FILE_NAME_TIME, "r")
    data = fileR.readline()
    file_creation_epoch_time = None
except FileNotFoundError:
    print("File Doesn't EXIST. Continuing the program by creating it..")
    # PART A
    file = open(FILE_NAME_TIME, "a")
    file_creation_epoch_time = int(time.time())
    file.write(f"CURRENT DATE TIME IS: {file_creation_epoch_time}")
    file.close()

if data:
    file_creation_epoch_time = int(data.split(':')[1].strip())

# PART B
seconds_passed = int(time.time() - file_creation_epoch_time)
print(f"{seconds_passed} seconds passed since the creation of file")

# PART C
# ANNUAL INTEREST IS 2.3%
annual_interest = 2.3
interest_in_an_year = float("{:.2f}".format(TOTAL_INVESTMENT * (annual_interest/100)))
interest_in_a_month = float("{:.2f}".format(interest_in_an_year/12))
interest_in_a_day = float("{:.2f}".format(interest_in_an_year/365))
interest_in_an_hour = float("{:.2f}".format(interest_in_a_day/24))
interest_in_a_minute = float("{:.2f}".format(interest_in_an_hour/60))
interest_in_a_second = float("{:.5f}".format(interest_in_a_minute/60))

print(f"You will earn ${interest_in_an_year} in an year on your capital investment of {TOTAL_INVESTMENT}")
print(f"You will earn ${interest_in_a_month} in a month on your capital investment of {TOTAL_INVESTMENT}")
print(f"You will earn ${interest_in_a_day} in a day on your capital investment of {TOTAL_INVESTMENT}")
print(f"You will earn ${interest_in_an_hour} in an hour on your capital investment of {TOTAL_INVESTMENT}")
print(f"You will earn ${interest_in_a_minute} in a minute on your capital investment of {TOTAL_INVESTMENT}")
print(f"You will earn ${interest_in_a_second} in a second on your capital investment of {TOTAL_INVESTMENT}\n")

# PART D & E
while True:
    seconds_passed = int(time.time()) - file_creation_epoch_time
    interest = '{:.3f}'.format(seconds_passed*interest_in_a_second)
    print(f"$1m + {interest} - Current Time is {time.ctime()}")
    time.sleep(3)
