import json
import requests
from django.shortcuts import render

app_name="lookup"

def getCityWeather(city):
    # use API to get data about a city's temperature
    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid=ed3db698182da566fc01319601b81ccd".format(city))

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = None
        
    try:
        temp = "{:0.2}".format(api["main"]["temp"] - 273.15)
    except:
        temp = None

    return city.capitalize(), temp

def home(request):
    if request.method == "POST":
        city = request.POST["city"]
    else:
        city = ""
    city, temp = getCityWeather(city)
    print(temp)
    print(city)
    context = {"temp": temp, "city": city}


    return render(request, "lookup/home.html", context)
