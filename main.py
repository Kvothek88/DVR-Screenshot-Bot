from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from PIL import ImageGrab
from PIL import ImageTk
import tkinter as tk
import csv
import time
import os
from config import *

# Function to capture screenshot
def capture_dvr(plant_list,plant):
    global offline_plants
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    try:
        driver.set_page_load_timeout(70)
        driver.get(plant_list[plant]["url"])
    except:
        isrunning = 0
        offline_plants.append([plant])
        driver.quit()
        return

    driver.maximize_window()

    time.sleep(45)
    username = driver.find_element(By.XPATH, '//input[@placeholder="User Name"]')
    username.send_keys(plant_list[plant]["user"])
    password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
    password.send_keys(plant_list[plant]["password"])
    driver.find_element(By.XPATH, "//button").click()

    time.sleep(45)
    if plant in strd_gui:
        driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]/i[contains(@class, 'icon-playall')]").click()
    elif plant in new_gui:
        driver.find_element(By.XPATH, "//button[@title='Start All Live View']").click()

    time.sleep(15)

    ss_region = (0,0,1920,1080)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))

    driver.quit()

# Function to run capture_dvr for all plants in plant_list
def run_capture_dvr(plant_list):
    global field
    global offline_plants
    for plant in plant_list:
        capture_dvr(plant_list,plant)
    if offline_plants:
        filename = get_variable_name(plant_list)
        file = open(os.path.join(cwd,f"{folder_name}",f"{filename} Offline Plants.csv"), 'w', newline ='')
        with file:
            write = csv.writer(file)
            write.writerow(field)
            write.writerows(offline_plants)
        offline_plants.clear()

def get_variable_name(variable):
    for name in globals():
        if id(globals()[name]) == id(variable):
            return name

root = tk.Tk()
root.title("DVR Screen Capture")

x = root.winfo_screenwidth()//2-250
y = int(root.winfo_screenheight()*0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

logo_img = ImageTk.PhotoImage(file="assets/cam.png")
logo_widget = tk.Label(frame1, image=logo_img,bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

button1 = tk.Button(
    frame1,
    text="PLANT GROUP 1",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_1))

button2 = tk.Button(
    frame1,
    text="PLANT GROUP 2",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_2))

button3 = tk.Button(
    frame1,
    text="PLANT GROUP 3",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_3))

button4 = tk.Button(
    frame1,
    text="PLANT GROUP 4",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_4))

button5 = tk.Button(
    frame1,
    text="PLANT GROUP 5",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_5))

button6 = tk.Button(
    frame1,
    text="PLANT GROUP 6",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_6))

button1.place(x=65,y=200)
button2.place(x=290,y=200)
button3.place(x=65,y=280)
button4.place(x=290,y=280)
button5.place(x=65,y=360)
button6.place(x=290,y=360)

root.mainloop()