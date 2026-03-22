import requests

# Coordinate for New York City (Look up philly lat/long)
lat = 40.71
lon = -74.01

lon = 75.09° N
lat = 39.57° W

# no "apikey"
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

# Accessing the data
current = data["current weather"]
temp = current["temperture"]
fahremheit = (temp * 1.8) + 32
print(f"Current Temperture:{temp}"C)
print(f"Wind Speed: {wind} km/h")


