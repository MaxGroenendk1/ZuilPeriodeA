print("Hello world!")
print("En hallo Martin Vreeburg, het is me eindelijk gelukt!")
# ----------- HIER ONDER ENKEL KLAD TE VINDEN----------------------
# import time
# mod_dtm = time.strftime('%Y-%d-%m')
# mod_thms = time.strftime('%H:%M:%S')
# print(mod_dtm + " " + mod_thms)

# #gebruik van een dict om een waarde te koppelen aan een gebruikers naam.
# gebruikersnaam = input("voer hier uw gebruikers naam in")
# while gebruikersnaam == gebruikersnaam:
#     wachtwoord = input("voer uw wachtwoord in")
#     if wachtwoord == huidigwachtwoord
#         # gebruikersnaam bepalen van gebruiker
#         gebruikersnaam = input("Voer uw gebruikersnaam in: ")
#         if gebruikersnaam == "":
#         print("wilt u anoniem blijven?: ")
#             print("(0)nee, (1)ja")
#             antwoord = input("Voer 0 of 1 in: ")
#             if antwoord == 1:
#                 gebruikersnaam == str("anoniem")
#                 print('Uw gebruikersnaam is:' + str(gebruikersnaam)
#                 elif antwoord == 0:
#                 gebruikersnaam = input("Voer uw gebruikersnaam in: ")
#
#                 # wachtwoord van gebruiker bepalen.
#                 # in een dict zetten en in bestand wegzetten.
#                 # gebruikersnamen herkennen en niet dubbel accepteren.
#                 # wachtwoord criteria geven.
# ____________________________________________________________________
# #plaats alle verkregen informatie in een lijst.
# # lst_info = [Comment, date_and_time(),costumerName,station_name()]
# lst_info = [costumerName, station_name(), date_and_time(), Comment]
# print(lst_info)
#
# fields = [Name, station_name(), date_and_time(), Comment] #simpele namen
# rows = [lst_info] #info gebruiker
#
# with open('Zuilberichten.txt', 'w') as f:
#     write = csv.writer(f)
#     write.writerow(fields)
#     write.writerows(rows)
# f.close()

#echter moet er aan deze lijst elementen wel een waarde worden gekoppeld, dus een dict is hier verstandig.
#lijst inladen met klant info
#nme = [costumerName]
#stt = [station_name()]
#dtt = [date_and_time()]
#cmt = [Comment]


#vorm klaarzetten om naar 'Zuilberichten.txt' te sturen
#dict = {'costumerName':nme, 'station_name':stt, 'date_and_time':dtt, 'Comment':cmt}
#directToFile = pandas.DataFrame(dict)
#directToFile.to_csv('Zuilberichten.txt')



#Extra AVG (eigen toevoeging) display toestemming tot openbaarmaking van de klant
#print("Dit bericht mag publiekelijk worden gemaakt?")
#displayable_message = input("type J(ja) of N(nee):")

#code die schrijven naar het txt bestand mogelijk maakt.
#opmerkingfile = open("Zuilberichten.txt", "w")
#opmerkingfile = open("Zuilberichten.txt", "a")
#opmerkingfile.write(dict)
#opmerkingfile.close()

#def message(dateTime,costumerName,):



#f = open('zuilberichten.txt' , 'r+')

# # bericht goedkeuren of afkeuren
# print('Keurt u dit bericht goed?')
# permission = input("type 1 voor 'ja', type 0 voor 'nee':")
# if permission == '1':
# # bij goedkeuring door schrijven naar db met deze data eraan toegevoegd;
# # -> of bericht goed is
# # -> datum+tijd van de beoordeling
# # -> naam van de moderator
# # -> het email adres van de moderator
# # mond uit op insert statement
#     print("Wilt u het volgende bericht controleren?")
# permission_continue = input("type 1 voor 'ja', type 0 voor 'nee':")
# if permission_continue == '1':
# # print volgende bericht!
#     if
# permission_continue == '0':
# # opnieuw of breakprogramma
#
# if permission == '0':
#     print("Wilt u het volgende bericht controleren?")
# permission_continue = input("type 1 voor 'ja', type 0 voor 'nee':")
# if permission_continue == '1':
# # print volgende bericht!
#     if
# permission_continue == '0':
# opnieuw of breakprogramma
#
# message_info = {
#     'user_name':[lst_info.append(costumerName)],
#     'location_name':[lst_info.append(station_name)],
#     'moment':[lst_info.append(date_and_time)],
#     'actual_message':[lst_info.append(Comment)]}
# print(message_info)
#
# df = pd.DataFrame(message_info, columns=['user_name', 'location_name', 'moment','actual_message'])
# print(df)
#
# new_val = df.index
# for x in new_val:
#     print(x + 1)
#
# #message_info = df.index()
#
#
# #for x in new_list_insertion:
#     #print(x)

# import tkinter as tk
# import tkinter.font as tkFont
#
# class App:
#     def __init__(self, root):
#         #setting title
#         root.title("undefined")
#         #setting window size
#         width=600
#         height=500
#         screenwidth = root.winfo_screenwidth()
#         screenheight = root.winfo_screenheight()
#         alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#         root.geometry(alignstr)
#         root.resizable(width=False, height=False)
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
