import time

import requests

CALENDER_API_KEY = "6ee4ea0704bf77c021818f6f3061db60a36c04fa"
WEATHER_API_KEY = "01d6a7ea5dbaee04a219feabea0c15c6"
COFFEE_API_URL = "https://coffee.alexflipnote.dev/random.json"


def get_holidays(country="CA", year="2020"):
    """
    This function will return all the holidays of the country with respect to the year.
    :param country:
    :param year:
    :return:
    """

    print("\nCalling Holiday API..")
    time.sleep(1)

    url = f"https://calendarific.com/api/v2/holidays?&api_key={CALENDER_API_KEY}&country={country}&year={year}"
    response = requests.get(url)
    response_holidays = response.json()['response']['holidays']
    _holidays = []
    for holiday in response_holidays:
        _holidays.append({
            'name': holiday['name'],
            'country': holiday['country']['name'],
            'date': holiday['date']['iso'],
            'states': holiday['states']
        })
    return _holidays


def get_coffee():
    """
    This function will return the coffee image.
    :return:
    """
    print("\nCalling Coffee API..")
    time.sleep(1)
    response = requests.get(COFFEE_API_URL)
    data = response.json()
    return data['file']


def weather_city(city="Sudbury"):
    """
    This function will print the weather of the city.
    :param city:
    :return:
    """
    print("\nCalling Weather API..")
    time.sleep(1)
    # URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'

    # Response from the API
    response = requests.get(url)

    # Converting into json
    data = response.json()

    # Converting into degree celsius.
    temp_c = data["main"]["temp"] - 273.15

    # Data Representation
    # print(f"Today, the temperature in {city.title()} is {round(temp_c, 2)}°C / {round(temp_c*(9/5)+32, 2)}°F / "
    #       f"{round(temp_c + 273.15, 2)}K as per the weather API.")

    # Create a dictionary to return data
    return {'K': round(temp_c+273.15, 2), 'C': round(temp_c, 2), 'F': round(temp_c*(9/5)+32, 2)}


def sunset_and_sunrise_time():
    """
    This function will tell you about the sunrise and sunset time of the specified region
    :return:
    """
    print("\nCalling Sunrise/Sunset timing API..")
    time.sleep(1)
    # Get the data from the aPI
    response = requests.get('http://api.sunrise-sunset.org/json?lat=46.522099&lng=-80.953033')
    # response = requests.get('http://api.sunrise-sunset.org/json?lat=24.8607&lng=67.0011')

    # Retrieving data
    data = response.json()['results']

    sunrise = str(int(data['sunrise'].split(':')[0])-4) + ":" + f":".join(data['sunrise'].split(':')[1:])
    sunset = str(int(data['sunset'].split(':')[0])-4) + ":" + f":".join(data['sunset'].split(':')[1:])
    sunset = sunset.replace("A", "P")

    return {'sunrise': sunrise, 'sunset': sunset}


def currency_convert(coins):
    """
    This API will convert the coin value to $
    1 coin worth $1000
    :param coins:
    :return:
    """
    # URL
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

    # QUERY STRING TO API
    querystring = {"format": "json", "from": "COIN", "to": "CAD", "amount": str(coins)}

    headers = {
        "X-RapidAPI-Key": "a90a556334mshdb8de176777bc97p179721jsn2d01896d03ed",
        "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if type(response) is str:
        return round(coins*1000, 2)

    # print(response.text)
    return round(coins*1000, 2)


try:
    # cup_of_coffee = coffee()
    # holidays = get_holidays(country="CA", year="2022")
    # weather = weather_city()
    # time = sunset_and_sunrise_time()
    # currency_convert(coins=10)
    pass
except Exception as e:
    print(str(e))
