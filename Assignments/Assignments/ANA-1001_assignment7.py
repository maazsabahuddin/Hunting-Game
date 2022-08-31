# Author: Maaz Sabah Uddin
# StudentId: A00257491
from urllib import request
import json


# Question 1
print("\n>>>>>>>>>>>>>>>>> QUESTION 01 >>>>>>>>>>>>>>>>>\n")


def astronautas():
    """
    This function will get the response from API and do the remaining work.
    :return:
    """
    # URL
    url = f'http://api.open-notify.org/astros.json'
    # API
    response = request.urlopen(url)
    # Converting into JSON
    result = json.loads(response.read())

    # EXTRACTING DATA AND PRINTING RESULT
    print(f"The current number of people in space are: {result['number']}")
    for people in result["people"]:
        print(f"The astronaut is {people['name']}")


astronautas()

# Question 2
print("\n>>>>>>>>>>>>>>>>> QUESTION 02 >>>>>>>>>>>>>>>>>\n")


def weather_city():
    """
    This function will print the weather of the city
    :return:
    """
    api_key = "01d6a7ea5dbaee04a219feabea0c15c6"
    # Karachi, Pakistan latitude and longitude
    city = "Karachi"

    # URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    # get the response from the API
    response = request.urlopen(url)
    # Converting into json
    data = json.loads(response.read())

    temp_c = data["main"]["temp"] - 273.15

    print(f"Today in {city.title()} the temperature is {round(temp_c, 2)}C")
    print(f"Low {round(data['main']['temp_min'] - 273.15, 2)}C")
    print(f"High {round(data['main']['temp_max'] - 273.15, 2)}C")


weather_city()


# Question 3
print("\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")

latitude = longitude = None


def space_station():
    """
    This function will return the lat long of space station
    :return:
    """
    # API
    url = f'http://api.open-notify.org/iss-now.json'

    # get the response from the API
    response = request.urlopen(url)

    # Converting into json
    result = json.loads(response.read())

    # get the lat long of that particular api..
    global latitude, longitude
    latitude = result["iss_position"]["latitude"]
    longitude = result["iss_position"]["longitude"]

    # forwarding **kwargs to iss function
    print(iss())


def iss():
    """
    This function will call the api to get the weather
    :return:
    """
    # API KEY
    api_key = '3ff0a790c6cf8eca1c62a178f252c718'
    # URL Below
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    # Getting API response
    response = request.urlopen(url)
    # Converting into json
    result = json.loads(response.read())

    if "country" in result["sys"]:
        return f'ISS is over {result["sys"]["country"]} and weather is {result["weather"]}'

    return f'ISS is over water and weather is {result["weather"]}'


space_station()

# Question 4
print("\n>>>>>>>>>>>>>>>>> QUESTION 04 >>>>>>>>>>>>>>>>>\n")


def sum_nums(*args):
    """
    This function will sum all the arguments
    :param args:
    :return:
    """
    _sum = 0
    for key in args:
        _sum += key

    print(f"The total sum is {_sum}")


sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
