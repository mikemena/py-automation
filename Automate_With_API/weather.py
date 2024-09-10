import Constants
import requests

appid = Constants.appid
baseUrl = "https://api.openweathermap.org/data/2.5/weather"
parameters = {"appid": appid, "zip": "33145", "country": "us"}

response = requests.get(baseUrl, params=parameters)

print(response.content)
