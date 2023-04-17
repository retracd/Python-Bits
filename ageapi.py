import requests

name = input("\t***Age Predictor***\nEnter a name: ")
response = requests.get(f"https://api.agify.io?name={name}")
#print(response.json())
print(f"The name, {name}, has a predicted age of {response.json()['age']}!")