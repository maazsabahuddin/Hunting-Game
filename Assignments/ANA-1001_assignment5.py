# Author: Maaz Sabah Uddin
# StudentId: A00257491
import random
import statistics

# Question 1
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 01 >>>>>>>>>>>>>>>>>\n")
myInfo = {'First Name': 'Maaz', 'Last Name': 'Sabah Uddin', 'Pizza Toping': 'Cheese', 'Age': 22, 'Sports': 'Football',
          'City': 'Karachi'}
for key, value in myInfo.items():
    print(f"{key} is {value}")

# Question 2
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 02 >>>>>>>>>>>>>>>>>\n")
friends = {'Maaz': ['Biryani', 'Tikka', 'Chicken'],
           'Swekshya': ['Tikka', 'Chicken', 'Biryani'],
           'Sahil': ['Podina', 'Mirchey', 'Chicken'],
           'Daniela': ['Tikka', 'Chicken', 'Mutton'],
           'Sophia': ['Biryani', 'Salad', 'Beef']}

for key, value in friends.items():
    print(f"{key} love all these dishes {value}")

# Question 3
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")

meals = [{'Maaz': ['Biryani', 'Tikka', 'Chicken']},
         {'Swekshya': ['Tikka', 'Chicken', 'Biryani']},
         {'Sahil': ['Podina', 'Mirchey', 'Chicken']},
         {'Daniela': ['Tikka', 'Chicken', 'Mutton']},
         {'Sophia': ['Biryani', 'Salad', 'Beef']}]

for meal in meals:
    print(f"{list(meal.keys())[0]} loves these foods {list(meal.values())[0]}")

# Question 4
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 04 >>>>>>>>>>>>>>>>>\n")
cities = {
    'Karachi': {'population': '30 million', 'facts': ['Most populated city', 'Biggest city', 'Generate most revenue.'],
                'country': 'Pakistan'},
    'Islamabad': {'population': '2 million', 'facts': ['Capital', 'Most cleanest city', 'Most IT Exports.'],
                  'country': 'Pakistan'}
}

for key, value in cities.items():
    print(f"City {key} city of {value['country']} got some greate information that is {value}")

# Question 5
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 05 >>>>>>>>>>>>>>>>>\n")
stock_prizes = {'StockA': [10, 12, 12.2, 13.1, 14, 15, 19, 21, 18.7],
                'StockB': [0.2, 1.2, 1.22, 1.31, 1.4, 1.5, 1.9, 2.1, 1.87],
                'StockC': [77, 87, 85, 83.1, 84, 95, 101, 101.5, 98]}

for key, value in stock_prizes.items():
    print(f'{key} overall price range {value}')
    print(f'{key} minimum prize ever {min(value)}')
    print(f'{key} minimum prize ever {max(value)}')
    print(f'{key} minimum prize ever {statistics.mean(value)}')

# Question 6
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 06 >>>>>>>>>>>>>>>>>\n")
popularity = 0
event_data = ['Event is great. Maaz scored century', 'Event has greate acoustic nosels', 'Lunch is fantastic',
              'Gaming area is legit', 'The function is really well organized.']
for i in range(5):
    random_popularity = random.randint(1, 15)
    popularity += random_popularity
    print(f'{event_data[i]} and gains {random_popularity}% popularity! Total popularity is now {popularity}%!')

print(f"The final result of popularity is {popularity}%")
if popularity > 51:
    print(f"Congratulation! You win")
else:
    print(f"You lose!")

# Question 7
print("\n\n>>>>>>>>>>>>>>>>> QUESTION 07 >>>>>>>>>>>>>>>>>\n")
_mydict = {1: 'Event is great. Maaz scored century', 2: 'Event has greate acoustic nosels',
           3: 'The function is really well organized.', 4: 12, 5: 12.2, 6: ['Maaz', 'Sahil'],
           7: ('Congratulation! You win', 'You lose!')}

for key, value in _mydict.items():
    if type(value) == str:
        print(f"{value.capitalize()}")
        print(f"{value.lower()}")
        print(f"{value.title()}")
