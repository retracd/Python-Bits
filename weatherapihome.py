import requests
from datetime import datetime, timedelta

zipcode = input("\t***Weekly Weather Forcast***\nPlease enter your zipcode: ") #gets user zipcode
zipdata = requests.get(f"https://api.zippopotam.us/us/{zipcode}") #contacts an api that gives coords of a zip
lon = zipdata.json()['places'][0]['longitude'] #extracts longitutude from data from api
lat = zipdata.json()['places'][0]['latitude'] #extracts latitude from data from api
weatherdata = requests.get(f"https://www.7timer.info/bin/api.pl?lon={lon}&lat={lat}&product=civillight&output=json")
# ^^^ uses latitude and longitude with a different, weather api to fetch weather info
for day in range(7): #loops 7 times for the 7 day forcast
    print((datetime.now() + timedelta(days=day)).strftime('%A')) #prints the name of the date + what iter of loop
    print(f"\tIt is going to look {weatherdata.json()['dataseries'][day]['weather']} today") #says weather for day
    tempMax = weatherdata.json()['dataseries'][day]['temp2m']['max'] #finds max of current day on loop
    print(f"\tWith a high of {round(tempMax * 1.8 + 32, 1)}F/{tempMax}C") #prints max in f and c
    tempMin = weatherdata.json()['dataseries'][day]['temp2m']['min'] #finds min of current day
    print(f"\tAnd a low of {round(tempMin * 1.8 + 32, 1)}F/{tempMin}C\n") #prints in f and c