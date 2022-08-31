# Author: Maaz Sabah Uddin
# StudentId: A00257491
import random
import time

PAUSE_TIME = 2

# Question 1
print("\n>>>>>>>>>>>>>>>>> QUESTION 01 >>>>>>>>>>>>>>>>>\n")
# Assigned nouns to a list
nouns = ['Gold', 'Painting', 'Advertisement', 'Grass', 'Parrot', 'Afternoon', 'Greece', 'Pencil', 'Airport', 'Guitar',
         'Piano', 'Ambulance', 'Hair', 'Pillow', 'Animal', 'Hamburger', 'Pizza']
# Assigned verbs to a list
verbs = ['Answer', 'Helicopter', 'Planet', 'Apple', 'Helmet', 'Act', 'Answer', 'Approve', 'Break', 'Build', 'Buy',
         'Color', 'Cough', 'Create', 'Cry', 'Dance', 'Describe', 'Drink', 'Eat', 'Edit']
# Assigned adverbs to a list
adverbs = ['abnormally', 'absentmindedly', 'accidentally', 'actually', 'adventurously', 'afterwards', 'almost',
           'always', 'annually', 'anxiously', 'arrogantly', 'awkwardly', 'bashfully', 'beautifully', 'bitterly']

# Taking user input
userInput = input("Do you want to read the unique story? Press q to quit: ")
# This while loop will run until user enters q either in small or capital
while userInput not in ['q', 'Q']:
    # randomly picking nouns verbs and adverbs
    print(f"Random Tales is a place where two writers collaborate together on a story. Each {random.choice(verbs)} on "
          f"alternate days, taking the story in a new {random.choice(nouns)}. Neither of them knows where the story "
          f"will take them to the place which is {random.choice(adverbs)}.\n")
    userInput = input("Do you want to read the another unique story? Press q to quit: ")

print("Thanks for listening the story!")


# PAUSE FOR 2 seconds
print(f"Pausing for {PAUSE_TIME} seconds...")
time.sleep(PAUSE_TIME)
print("Pause End")


# Question 2
print("\n>>>>>>>>>>>>>>>>> QUESTION 02 >>>>>>>>>>>>>>>>>\n")
player = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
computer = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

playerPoints = 0
computerPoints = 0
points = 0


def is_draw(cardA, cardB):
    """
    This function will tell whether both cards are same or not
    :param cardA:
    :param cardB:
    :return:
    """
    return cardA == cardB


def get_higher_card_winner(cardA, cardB):
    """
    This function will return the highest value card
    :param cardA:
    :param cardB:
    :return:
    """
    if type(cardA) is int and type(cardB) is int:
        if cardA > cardB:
            return cardA, None
        else:
            return None, cardB
    elif type(cardA) is str and type(cardB) is str:
        if cardA == 'Ace':
            return cardA, None
        elif cardB == 'Ace':
            return None, cardB
        elif cardA == 'King':
            return cardA, None
        elif cardB == 'King':
            return None, cardB
        elif cardA == 'Queen':
            return cardA, None
        elif cardB == 'Queen':
            return None, cardB
        elif cardA == 'Jack':
            return cardA, None
        elif cardB == 'Jack':
            return None, cardB
    elif type(cardA) is str and type(cardB) is int:
        return cardA, None
    elif type(cardB) is str and type(cardA) is int:
        return None, cardB
    return None, None


# This while loop will run until one of these player or computer list is not empty
while player and computer:
    random.shuffle(player)
    random.shuffle(computer)
    playerChoice = random.choice(player)
    computerChoice = random.choice(computer)

    if is_draw(cardA=playerChoice, cardB=computerChoice):
        points += 1
        player.remove(playerChoice)
        computer.remove(computerChoice)
        continue

    points += 1
    playerWin, computerWin = get_higher_card_winner(cardA=playerChoice, cardB=computerChoice)
    if playerWin:
        playerPoints += points
    else:
        computerPoints += points

    points = 0
    player.remove(playerChoice)
    computer.remove(computerChoice)

print(f"The final score of player is {playerPoints} and, \nthe final score of computer is {computerPoints}\nHence, ")
if playerPoints > computerPoints:
    print("Player Wins! The game.")
else:
    print("Computer Wins! The game.")


# PAUSE FOR 2 seconds
print(f"\nPausing for 2 seconds...")
time.sleep(PAUSE_TIME)
print("Pause End")


# Question 3
print("\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")
print("WELCOME TO PIZZA STORE\n")
name = input("Please, enter your name: ")
print("Pizzas prices: \n1- small $6.99\n2- medium $8.99\n3- large $10.99\n")
pizza_price = {1: 6.99, 2: 8.99, 3: 10.99}
try:
    pizza_choice = int(input("Enter your choice: "))
    # This while loop will run until user enters a correct number inbetween 1 to 3
    while pizza_choice < 1 or pizza_choice > 3:
        pizza_choice = int(input("Invalid option selected. Enter your choice: "))
    pizza_quantity = int(input("Enter quantity: "))
    # This while loop will run until user enters a correct number which is greater than 0
    while pizza_quantity < 1:
        pizza_quantity = int(input("Pizza quantity cannot be less than 1. Enter your choice: "))
except ValueError as e:
    # In an error case system willexit
    print("Invalid option selected. Please re-run the program. ")
    raise SystemExit

amount = pizza_price[pizza_choice] * pizza_quantity
tax = amount * 0.13
amount_with_tax = amount * 1.13

print(f"\n\nName: {name}")
print(f"Pizza Choice: {pizza_choice}")
print(f"Pizza Quantity: {pizza_quantity}")
print(f"Total: {amount}")
print(f"Tax: {tax}")
print(f"Total Amount + Tax: {amount_with_tax}")

# PAUSE FOR 2 seconds
print(f"\nPausing for 2 seconds...")
time.sleep(PAUSE_TIME)
print("Pause End")


# Question 4
print("\n>>>>>>>>>>>>>>>>> QUESTION 04 >>>>>>>>>>>>>>>>>\n")
dinner_cost = 0
counter = 1
members_age = []
members_cost = []
userInput = int(input('How many members are you for the party: '))
while userInput > 0:
    members_age.append(int(input(f'Enter Member {counter} age: ')))
    userInput -= 1
    counter += 1

for age in members_age:
    if age < 5:
        dinner_cost += 0
        members_cost.append(0)
    elif age < 10:
        dinner_cost += 5
        members_cost.append(5)
    elif age < 18:
        dinner_cost += 10
        members_cost.append(10)
    elif age < 65:
        dinner_cost += 12
        members_cost.append(12)
    else:
        dinner_cost += 15
        members_cost.append(15)

tax = dinner_cost * 0.08
total_cost = dinner_cost + tax
print(f"The total number of members are: {len(members_age)}")
print(f"The dinner cost is: {dinner_cost}")
print(f"The total dinner tax is: {tax}")
print(f"The total dinner cost is: {total_cost}")
print(f"The avg cost of dinner is: {(dinner_cost+tax)/ len(members_age)}")
print(f"The total for each dinner is as follows: ")
c = 1
for cost in members_cost:
    print(f"Member {c} dinner cost is {cost*1.08}")
    c += 1

print("ALL DONE!")
