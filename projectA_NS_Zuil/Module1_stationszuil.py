import datetime
import random
import csv
import eel


def get_now():
    ''' Deze functie bepaald de huidige tijd middels een bibliotheek, en rond vervolgens de overige decimalen af.'''
    now = datetime.datetime.now().timestamp()
    return now
    # formetted_now = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    # return formetted_now # [:-7] # -7 als je de punt -> "." ook weg wilt, maar is handig om te gebruiken en wellicht later op te splitten


eel.init('web')


@eel.expose
def get_stations():
    with open("Station_locatie.txt", "r+") as file:
        stations = file.read().split('\n')

    return stations


@eel.expose
def post_message(message, name, station):

    if message == "" or len(message) > 140:
        return False

    if name == "":
        name = "anoniem"

    record = [name, station, get_now(), message]

    # #schrijft in csv bestand
    with open('Zuilberichten.csv', 'a', newline='') as file:
        writer_object = csv.writer(file)
        writer_object.writerow(record)

    return True


eel.start('GUImodule1.html')


#
#
# #plaats alle verkregen informatie in een lijst.
# # lst_info = [comment, date_and_time(),costumerName,station_name()]
# lst_info = [costumerName, station_name(), date_and_time(), comment]
# print(lst_info)
#
# #schrijft in csv bestand
# with open('Zuilberichten.csv', 'a', newline='') as file_object:
#     writer_object = csv.writer(file_object)
#     writer_object.writerow(lst_info)
#
# # # in Json gezet.
# # with open ('Zuilberichten.csv', 'r') as file_object: # enkel lezen
# #     # haalt alles op uit het bestand zuilberichten en slaat het op in variable berichten.
# #     berichten = json.load(file_object) #berichten is lijst met lijsten
# #     print(berichten)
# #     berichten.append(lst_info)
# #
# # with open('Zuilberichten.csv', 'w+') as file_object: #als je nu het bestand wist zonder + geeft die aan dat het bestand niet bestaat
# #     # dumpt de lijst in het bestand.
# #     json.dump(berichten, file_object, indent= 4)
#
#
#
#
# #def submit_comment(costumerName, station_name(), date_and_time(), comment):
