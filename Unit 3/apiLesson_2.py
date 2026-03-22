# API - Application Programming Interface
# Allows computers to share data between devices
# via the internet.

# functions thyat let us share data back and forth over
# the internet

import requests # modules -->
#is object with methodsd and properties that
# were already written/prewritten for us

data = requests.get('https://restcountries.com/v3.1/all?fields=name')

print(data)
print(data.json())

# Use the API to find data on 1 African Country,
# 1 South American Country, and 1 asian Country. You should have 3
# variable returning data for each type of country.

# 1. African Country (Nigeria):
african_request = requests.get()

africanCountry = requests.get('https://restcountries.com/v3.1/name/nigeria')
asianCountry = requests.get('https://restcountries.com/v3.1/name/nsouth korea')
sAmericanCountry = requests.get('https://restcountries.com/v3.1/name/columbia')