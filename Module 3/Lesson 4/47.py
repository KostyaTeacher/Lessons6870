import requests

NUMBER_OF_INDEX = 20

respons = requests.get("https://rickandmortyapi.com/api/character")
print(respons)
print("")
print("")
answer = respons.json()
for i in range(NUMBER_OF_INDEX):
    print(answer["results"][i]["name"])
    print(answer["results"][i]["species"])
    print(answer["results"][i]["status"])
print(answer)