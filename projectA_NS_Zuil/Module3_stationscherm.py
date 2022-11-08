import psycopg2
import requests
import random
import csv

conn = psycopg2.connect(database="ns_projecta", user="postgres", password="mydb123", host="127.0.0.1", port="5432")
cur = conn.cursor()


def station_locatie():
    ''' achter haalt de stations waarop een bericht is geschreven die in de database zijn gezet'''
    cur.execute("SELECT DISTINCT station "
                "FROM messages")
    conn.commit()
    return cur.fetchall()


station_list = station_locatie()
station_as_tuple = random.choice(station_locatie())
api_key = "86a37d514f009078a9c38d03dbb15cb9"
station = station_as_tuple[0]


def city_weather_info():
    ''' Laat het weer zien van ingevoerde stad gebaseerd op uitkomst funtie "station_name" '''
    URL = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={station}&appid={'86a37d514f009078a9c38d03dbb15cb9'}&lang=nl").json()
    Weather = (URL["weather"][0]["description"])
    return Weather

# Query:display laatste 5 berichten uit db
def recent_messages():
    ''' achter haalt de laatste 5 berichten die zijn toegevoegd aan de database d.m.v datum & tijd'''
    cur.execute("SELECT messages.name_customer, messages.station, messages.comment, messages.commented_on "
                "FROM messages "
                "WHERE evaluation = TRUE "
                "ORDER BY commented_on DESC "
                "LIMIT 5")
    conn.commit()
    return cur.fetchall()


for message in recent_messages():
    print(message[0] + " @", message[1] + ";", message[2] + "| Ingevoerd op;", str(message[3]))
message_activity = (message[0] + " @", message[1] + ";", message[2] + "| Ingevoerd op;", str(message[3]))
print(message[1])

# for column in cur.fetchall():
#     if column_name in column:
#         dictionary["name_customer"] = column[1]
#         dictionary["station"] = column[2]
#         dictionary["comment"] = column[3]
#         dictionary["commented_on"] = column[4]


def facility_services():
    ''''Query: display facaliteiten op alle station van de berichten die zijn goedgekeurd '''
    # -> omzetten van true en false naar aanwezig en niet-aanwezig
    # OOK ENKEL SELECTEREN VAN STATION WAAR BERICHT IS INGEVOERD:
    # gebruik "city_location_user"

    cur.execute(
        "SELECT station_service.station_city, station_service.ov_bike, station_service.elevator, station_service.toilet, station_service.park_and_ride "
        "FROM messages "
        "INNER JOIN station_service ON station = station_city "
        "WHERE evaluation = TRUE")  # ? AND "{city_location_user}" == "station.service station_city"?
    conn.commit()
    return cur.fetchall()


for row in facility_services():
    first_result = (row)

#deze file bevat:
    with open("actieve_stations.txt", 'a+', newline='') as file:
        writer_file= csv.writer(file, lineterminator = '\n')
        writer_file.writerow(row)
        #writer_file.writerows(row)

with open('actieve_stations.txt', 'r') as active_file:
    reader = csv.reader(active_file)

    for row in reader:
        station = row[0]
        ov_bike = row[1]
        elevator = row[2]
        toilet = row[3]
        park_and_ride = row[4]
specific_location_info = [station, ov_bike, elevator, toilet, park_and_ride]
print(specific_location_info)

# --- doel ---
# csv file doorloopt nog niet alle lijnen, optie keuze toevoegen van alle stations
# Leest de 1 tot 4 elementen uit de lijst juist door, de code hieronder verwijst naar statements "True" maar print onjuiste informatie naar de gebruiker.
print(specific_location_info[1])
if station == specific_location_info[0]:
    if specific_location_info[1] == True:
        print("Op dit station kan een OV-fiets worden gehuurd")
    else:
        print("Op dit station kan GEEN OV-fiets worden gehuurd")
    if specific_location_info[2] == True:
        print("Op dit station kan een lift worden gebruikt")
    else:
        print("Op dit station kan GEEN lift worden gebruikt")
    if specific_location_info[3] == True:
        print("Op dit station kan een toilet worden gebruikt")
    else:
        print("Op dit station kan GEEN toilet worden gebruikt")
    if specific_location_info[4] == True:
        print(("Op dit station kan een P+R worden gebruikt"))
    else:
        print(("Op dit station kan GEEN P+R worden gebruikt"))


#--------------------------------------KLAD----------------------------------------------------------
# for row in facility_services():
#     ''' geeft int(x) <-- aantal lijsten'''
#     first_result = len(row)
#     #first_result = len(facility_services())
#     for each row
#
#     print(first_result)
#
# for first_result in facility_services():
#     result = first_result
#     print(result)
#
#
# with open('actieve_station.txt', 'a', newline='') as inactive_message_file:
#     writer_object = csv.writer(inactive_message_file)
#     writer_object.writerow(result)
#
# #haalt lijn uit txt bestand en zet neer
# with open('actieve_station.txt', 'r') as active_message_file:
#     reader = csv.reader(active_message_file)
#
#     for row in reader:
#         station = row[0]
#         ov_bike = row[1]
#         toilet = row[2]
#         park_and_ride = row[3]
#
# specific_location_info = [station, ov_bike, toilet, park_and_ride]
# print(specific_location_info)

#for result in first_result:

    #print(first_result[0]) --> enkel laatste stad 5 keer
    #print (first_result) --> laatste lijst 5 keer
    #print (facility_services())

# amount_of_cities = len(facility_services())
# print(amount_of_cities)
# list = amount_of_cities/amount_of_cities
# facility = [1 tot 4]
# amount_of_cities * facility


#print (len(facility_services()))*(len(facility_services()[0]))

#print(lst_of_city)
#naam stad verkrijgen



# for stad_met_attribuut in facility_services():
#     print stad_met_attribuut
# # if station_locatie() == achter halen uit fetch.facility
#
# dictionary = {}
# for column in cur.fetchall():
#     if column_name in column:
#         dictionary["station_city"] = column[1]
#         dictionary["ov_bike"] = column[2]
#         dictionary["elevator"] = column[3]
#         dictionary["toilet"] = column[4]
#         dictionary["park_and_ride"] = column[5]
#         if dictionary['ov_bike']:
#             print("Op dit station kan een OV-fiets worden gehuurd")
#         if dictionary["elevator"]:
#             print("Op dit station kan een lift worden gebruikt")
#         if dictionary["toilet"]:
#             print("Op dit station kan een toilet worden gebruikt")
#         if dictionary["park_and_ride"]:
#             print("Op dit station kan een P+R worden gebruikt")
# #wat ik terug krijg uit "cur.execute" wil ik in een DICT zetten en variabele van eerste column uitlezen
# #dict result column 1 [1] = "station_city"
# #if "city_location_user" ==  "station_city"
#   #print (