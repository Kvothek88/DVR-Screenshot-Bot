from datetime import date
import os

today = date.today()
today = today.strftime("%b-%d-%Y") 

folder_name = str(today)

# Check if folder does not already exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

cwd = os.getcwd()

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

# GUI lists
strd_gui = ["Plant 1","Plant 3","Plant 4","Plant 6","Plant 8","Plant 9","Plant 11","Plant 12","Plant 13","Plant 17","Plant 18","Plant 19","Plant 20","Plant 21","Plant 22","Plant 23","Plant 33","Plant 34","Plant 39","Plant 40"]
new_gui = ["Plant 2","Plant 5""Plant 7","Plant 10","Plant 14","Plant 15","Plant 16","Plant 24","Plant 25","Plant 26","Plant 27","Plant 28","Plant 29","Plant 30","Plant 31","Plant 32","Plant 35","Plant 36","Plant 37","Plant 38"]

# Offline plants list
field = ["Offline Plants"]
offline_plants = []