import datetime
import random
import csv
import pandas as pd
import json

#verkrijg het bericht van klant
print("Heeft u een opmerking, mening of een compliment voor de NS?(maximaal 140 karakters)")
Comment = input("Voer hier uw bericht in:")
if len(Comment) > 140:
    print("Bericht is te lang!")
    Comment = input("Voer hier uw bericht in:")

#verkrijg de datum & tijd (in een functie gezet want anders moet iedere keer deze code apart geschreven worden om de decimalen eraf te halen).
def date_and_time():
    ''' Deze functie bepaald de huidige tijd middels een bibliotheek, en rond vervolgens de overige decimalen af.'''
    time = datetime.datetime.now()
    #new_date = datetime.datetime.now().date() <- enkel de datum
    #new_time = datetime.datetime.now().time() <- wel ondersteund maar het antwoord aanpassen zonder functie niet ondersteund.
    new_date_and_time = time.strftime('%Y-%m-%d %H:%M:%S.%f')
    return new_date_and_time[:-7] # -7 als je de punt -> "." ook weg wilt, maar is handig om te gebruiken en wellicht later op te splitten
#verkrijg de naam van de klant of anoniem

print("indien u geen naam in wilt voeren, druk enter, u gaat door als 'anoniem'")
costumerName = input("Voer hier uw naam in (maximaal 51 karakters):")
if costumerName == '':
    costumerName = "anoniem"

#verkrijg van stationlocatie
def station_name():
    ''' Deze functie kiest het middelste eelement uit een lijst bestaande uit 3 elementen, van 3 willekeurig gekozen lijnen uit het document 'Station_locatie.txt' '''
    stationName = open("Station_locatie.txt", "r+")
    all_station_names = stationName.read().split('\n')
    random_station_names = random.sample(all_station_names, 3)
    pick_mid_from_list = random_station_names[1]
    stationName.close()
    return pick_mid_from_list

#plaats alle verkregen informatie in een lijst.
# lst_info = [Comment, date_and_time(),costumerName,station_name()]
lst_info = [costumerName, station_name(), date_and_time(), Comment]
print(lst_info)

#schrijft in csv bestand
with open('Zuilberichten.txt', 'a', newline='') as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerow(lst_info)

# # in Json gezet.
# with open ('Zuilberichten.txt', 'r') as file_object: # enkel lezen
#     # haalt alles op uit het bestand zuilberichten en slaat het op in variable berichten.
#     berichten = json.load(file_object) #berichten is lijst met lijsten
#     print(berichten)
#     berichten.append(lst_info)
#
# with open('Zuilberichten.txt', 'w+') as file_object: #als je nu het bestand wist zonder + geeft die aan dat het bestand niet bestaat
#     # dumpt de lijst in het bestand.
#     json.dump(berichten, file_object, indent= 4)




#def submit_comment(costumerName, station_name(), date_and_time(), Comment):
