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

url = "https://rickandmortyapi.com/api/character"
res = requests.get(url)
print(res.status_code)


if res.status_code == 200:
    charData = re.json()
    filtData ={
        "name":charData["name"],
        "gender":charData["gender"],
        "image":charData["image"]
    }
    print(filtData)

else:
    print("somethings went wrong...")
    print(res.status_code)
