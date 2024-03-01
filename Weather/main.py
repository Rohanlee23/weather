import requests
import json

API = "1a5bdbc0ee6144dcb72131751242102"

aqi = "yes"
city_name = input("Enter city name to gets its weather report: ")
url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"
result = requests.get(url)
print(result)
wdata = json.loads(result.text)
print(wdata)

name = wdata["location"]["name"]
region = wdata["location"]["region"]
temp = wdata["current"]["temp_c"]
humidity = wdata["current"]["humidity"]

print(name)
print(humidity)
print(temp)