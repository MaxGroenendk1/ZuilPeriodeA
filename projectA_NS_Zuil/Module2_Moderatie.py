#deze leest de gegevens uit het "zuilberichten.txt" bestand & leest de berichten uit de open weather map vai een api koppeling

import time
from datetime import datetime
import csv
import psycopg2


#verbinding maken met db
conn = psycopg2.connect(database="ns_projecta", user="postgres", password="mydb123", host="127.0.0.1", port="5432")
cur = conn.cursor()#positie in db veld aanroepen


#query klaarzetten en inladen in messages tabel
def insertion_mod(name, station, date_time, comment, evaluation, evaluation_on, name_mod, email_mod):
    cur.execute(f"INSERT INTO messages (name_customer, station, comment, commented_on, name_mod, email_mod, evaluation, evaluated_on)"
                f"VALUES ('{name}', '{station}', '{comment}','{datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')}', '{name_mod}', '{email_mod}','{evaluation}','{evaluation_on}')")
    conn.commit()

#moderator naam en email verkrijgen
print("Om de berichten van de NS te mogen beoordelen dient u volgende gegevens in te vullen")
name_mod = input("Voer uw moderator-naam in:")
email_mod = input("Voer uw email in:")

lst_of_messages = []
with open('Zuilberichten.txt', 'r') as message_file:
    reader = csv.reader(message_file)

    for row in reader:
        name = row[0]
        station = row[1]
        date_time = row[2]
        comment = row[3]
message = [name, station, date_time, comment]

print(message)

#bericht goedkeuren of afkeuren
print("Keurt u dit bericht goed?")
evaluation = int(input("Ja = typ '1' (True) /Nee = typ '0' (false)"))
evaluation_on = str(datetime.now())

data = [name, station, date_time, comment, evaluation, evaluation_on, name_mod, email_mod]
insertion_mod(name, station, date_time, comment, evaluation, evaluation_on, name_mod, email_mod)
print('Toegevoegd aan db:')
print(data)

#haalt de laatst beoordeelde lijn uit het csv bestand.
with open('Zuilberichten.txt', 'r+') as adjust_file:
    lines = adjust_file.readlines()
    adjust_file.seek(0)
    adjust_file.truncate()
    adjust_file.writelines(lines[:-1])


