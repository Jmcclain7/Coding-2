# Use ONE of the following APIs to pull and access the data.

# Dog API -> return at least 3 types of dogs 
# https://dog.ceo/dog-api/

url = "https://dog.ceo/dog-api/"
res = requests.get(url)

print(res)
print(res.json())



# Cat API -> return at least 3 types of cats
# https://http.cat/

# Rick and Morty API -> return at least 3 rick and morty characters
# https://rickandmortyapi.com/

import requests
url = "https://rickandmortyapi.com/api/character"

if response.status_code == 200:
    data = response.json()


    characters = data['results']

    print("Rick and Morty Characters")