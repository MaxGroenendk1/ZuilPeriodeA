#api ophalen
import random
import requests
import psycopg2
import json

conn = psycopg2.connect(database="ns_projecta", user="postgres", password="mydb123", host="127.0.0.1", port="5432")
cur = conn.cursor()


def station_locatie():
    ''' achter haalt de stations waarop een bericht is geschreven die in de database zijn gezet'''
    cur.execute("SELECT DISTINCT station "
                "FROM messages ")

    conn.commit()
    return cur.fetchall()

print(station_locatie())
x_first = (station_locatie())
x = x_first.split
print(x)

api_key= "86a37d514f009078a9c38d03dbb15cb9"
def station_name():
    ''' Deze functie kiest het middelste eelement uit een lijst bestaande uit 3 elementen, van 3 willekeurig gekozen lijnen uit het document 'Station_locatie.txt' '''
    stationName = open("Station_locatie.txt", "r+")
    all_station_names = stationName.read().split('\n')
    random_station_names = random.sample(all_station_names, 3)
    pick_mid_from_list = random_station_names[1]
    stationName.close()
    return pick_mid_from_list
print(station_name())
stad = str(station_name()) #dynamisch maken door stad op te pakken uit
def stad_info():
    URL = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={stad}&appid={'86a37d514f009078a9c38d03dbb15cb9'}&lang=nl").json()
    Weather = (URL["weather"][0]["description"])
    print(Weather)

stad_info()