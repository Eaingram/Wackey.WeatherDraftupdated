import urllib3, urllib, json, requests
from pprint import pprint #import pretty print
api_key = "78f8a413a400c52f7816c1e52cdc4e69"

print("Welcome to my Wackey Weather viewer")

zip_or_city=input("Enter 'z' for zipcode or 'c' for city")
base_url = "http://api.openweathermap.org/data/2.5/weather?"

if zip_or_city == 'z':
    zipcode=input("please enter zip code")
    complete_url = base_url + "zip=" + zipcode + "&appid=" + api_key

if zip_or_city == 'c':
    city=input("please enter city")
    complete_url = base_url + "q=" + city + "&appid=" + api_key

print(complete_url)
response = requests.get(complete_url)
weatherJson = response.json()

print(weatherJson)

if weatherJson['cod'] == 200:
    parsedJson = weatherJson["main"]

    # get current temperature
    current_temperature = parsedJson["temp"]

    # get current pressure
    current_pressure = parsedJson["pressure"]

    # get current humidity
    current_humidity = parsedJson["humidity"]

    # store weather
    weather = weatherJson["weather"]

    # get weather description from weather
    weather_description = weather[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))
else:
    print("API query failed")
