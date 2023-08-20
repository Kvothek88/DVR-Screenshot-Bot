from datetime import date
import csv
import os

today = date.today()
today = today.strftime("%b-%d-%Y") 

folder_name = str(today)

cwd = os.getcwd()

# Check if folder does not already exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

bg_color = "#009966"

# Dictionary where 'Key:Value' pair is 'Plant name:Dvr credentials'
PLANT_GROUP_1 = {"Plant 1":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 2":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 3":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 4":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 5":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 6":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 7":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

PLANT_GROUP_2 = {"Plant 8":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 9":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 10":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 11":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 12":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 13":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 14":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 15":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 16":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 17":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 18":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

PLANT_GROUP_3 = {"Plant 19":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 20":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 21":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 22":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 23":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 24":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

PLANT_GROUP_4 = {"Plant 25":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 26":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 27":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 28":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 29":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 30":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 31":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

PLANT_GROUP_5 = {"Plant 32":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 33":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 34":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 35":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 36":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 37":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

PLANT_GROUP_6 = {"Plant 38":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 39":{"url":"https://somesite.com/login","user":"admin","password":"????????"},
                 "Plant 40":{"url":"https://somesite.com/login","user":"admin","password":"????????"}}

blacklist = ["Fotolefkada","Fotoandros","Fototrikala 500","Fototrikala 1MW","Astreches 61","Astreches 51","Retziki","Magoules 49",
             "Magoules 47","Doxara","Psichiko","Amygdalia","Ierapetra 40 Mikro","Ierapetra 40 Megalo"]

# Offline plants list
field = ["Offline Plants"]
offline_plants = []
# Captured Plants list in order to not take photo again
field2 = ["Captured Plants"]
captured_plants = []

# If it does not exist create Captured Plants csv, else the plants in csv and append them in captured_plants list 
if not os.path.exists(os.path.join(cwd,f"{folder_name}","Captured Plants.csv")):
    file2 = open(os.path.join(cwd,f"{folder_name}","Captured Plants.csv"), 'w', newline ='')
    with file2:
        write = csv.writer(file2)
        write.writerow(field2)
else:
    with open(os.path.join(cwd,f"{folder_name}","Captured Plants.csv"), 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            captured_plant = row[0]
            captured_plants.append(captured_plant)
