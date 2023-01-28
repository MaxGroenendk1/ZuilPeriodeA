import psycopg2
import requests
import eel

OPEN_WEATHER_API_KEY = "86a37d514f009078a9c38d03dbb15cb9"

conn = psycopg2.connect(database="ns_projecta", user="postgres", password="mydb123", host="127.0.0.1", port="5432")
cur = conn.cursor()

eel.init('web')


@eel.expose
def get_stations():
    with open("Station_locatie.txt", "r+") as file:
        stations = file.read().split('\n')

    return stations


@eel.expose
def get_weather(station):
    ''' Laat het weer zien van ingevoerde stad gebaseerd op uitkomst funtie "station_name" '''
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={station}&appid={OPEN_WEATHER_API_KEY}&lang=nl"
    response = requests.get(URL).json()
    weather = response["weather"][0]["description"]
    return weather


@eel.expose
def get_messages():
    ''' Query: display facaliteiten op alle station van de berichten die zijn goedgekeurd '''
#query is bij het select statement specifiek aangezien python precies de informatie nodig heeft die opgevraagd wordt door de gebruiker.
#SQL kan informatie ook verkrijgen zonder dat hij alles hoeft op te roepen dat gebeurt al bij een innerjoin, echter zal het bij de display van python
#essentiele data missen.
    cur.execute(
            "SELECT messages.name_customer, messages.station, messages.comment, station_service.ov_bike, station_service.elevator, station_service.toilet, station_service.park_and_ride "
            "FROM messages "
            "INNER JOIN station_service ON station = station_city "
            "WHERE messages.evaluation = TRUE "
            "ORDER BY commented_on DESC "
            "LIMIT 5 ")
    conn.commit()
    return cur.fetchall()


eel.start('GUImodule3.html')
