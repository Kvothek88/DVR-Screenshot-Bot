from datetime import date
from data import *
import csv
import os

today = date.today()
today = today.strftime("%b-%d-%Y")
delay = 10
folder_name = str(today)

cwd = os.getcwd()

# Check if folder does not already exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

bg_color = "#009966"

blacklist = ["Plant 3","Plant 4","Plant 14","Plant 15","Plant 23","Plant 37","Plant 39"]

slow_plants = ["Plant 3","Plant 6","Plant 27"]

very_slow_plants = ["Plant 3","Plant 3"]

# Offline plants list
field = ["Offline Plants"]
field2 = ["Captured Plants"]
offline_plants = []
captured_plants = []

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
