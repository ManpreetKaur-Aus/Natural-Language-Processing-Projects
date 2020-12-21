import requests

def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=ddd9d52ec65f3473684f12dd1974c8db&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']
    print(weather_main)
    return weather_main