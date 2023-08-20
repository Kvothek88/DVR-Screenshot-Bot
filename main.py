from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from PIL import ImageGrab
from PIL import ImageTk
import tkinter as tk
import pyautogui
import csv
import time
import os
from config import *

# Function to capture screenshot
def capture_dvr(plant_list,plant):
    global offline_plants
    global blacklist
    if plant_list[plant]["gui"] != "ever" and plant not in blacklist:

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        try:
            driver.set_page_load_timeout(40)
            driver.get(plant_list[plant]["url"])
        except:
            offline_plants.append([plant])
            driver.close()
            return

        driver.maximize_window()

        time.sleep(10)

        username = driver.find_element(By.XPATH, '//input[@placeholder="User Name"]')
        username.send_keys(plant_list[plant]["user"])
        password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password.send_keys(plant_list[plant]["password"])
        driver.find_element(By.XPATH, "//button").click()

        time.sleep(25)
        
        if plant_list[plant]["gui"] == "hik-1":
            driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]/i[contains(@class, 'icon-playall')]").click()
        elif plant_list[plant]["gui"] == "hik-2":
            driver.find_element(By.XPATH, "//button[@title='Start All Live View']").click()

        time.sleep(10)

        ss_region = (0,0,1920,1080)
        ss_img = ImageGrab.grab(ss_region)
        ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))

        driver.close()

    elif plant_list[plant]["gui"] != "ever" and plant in blacklist:
        driver = webdriver.Ie(service=Service(IEDriverManager().install()))          
        try:
            driver.set_page_load_timeout(5)
            driver.get(plant_list[plant]["url"])
        except:
            if plant == "Fotolefkada":
                time.sleep(10)
            pyautogui.moveTo(1070,600,duration=1)
            pyautogui.click()
            pyautogui.typewrite(plant_list[plant]["user"],interval=0.1)
            pyautogui.moveTo(1070,650,duration=1)
            pyautogui.click()
            pyautogui.typewrite(plant_list[plant]["password"],interval=0.1)
            pyautogui.moveTo(1070,720,duration=1)
            pyautogui.click()
            driver.maximize_window()
            if plant == "Fotolefkada":
                time.sleep(15)
            else:
                time.sleep(5)
            if plant_list[plant]["gui"] == "hik-1":
                try:
                    driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]/i[contains(@class, 'icon-playall')]").click()
                except:
                    time.sleep(5)
                    ss_region = (0,0,1920,1080)
                    ss_img = ImageGrab.grab(ss_region)
                    ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))
                    pyautogui.moveTo(1900,30,duration=0.5)
                    pyautogui.click()                     
            elif plant_list[plant]["gui"] == "hik-2":
                try:
                    driver.find_element(By.XPATH, "//button[@title='Start All Live View']").click()
                except:
                    time.sleep(5)
                    ss_region = (0,0,1920,1080)
                    ss_img = ImageGrab.grab(ss_region)
                    ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))
                    pyautogui.moveTo(1900,30,duration=0.5)
                    pyautogui.click()                     
    else:
        driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        try:
            driver.set_page_load_timeout(4)
            driver.get(plant_list[plant]["url"])
        except:
            pyautogui.moveTo(550,700,duration=2)
            pyautogui.click()
            time.sleep(5)
            driver.maximize_window()
            time.sleep(7)
            ss_region = (0,0,1920,1080)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg")) 
            driver.close() 

# Function to run capture_dvr for all plants in plant_list
def run_capture_dvr(plant_list):
    global field
    global offline_plants
    global captured_plants

    for plant in plant_list:
        if plant not in captured_plants:
            capture_dvr(plant_list,plant)
            captured_plants.append([plant])
            file = open(os.path.join(cwd,f"{folder_name}","Captured Plants.csv"), 'a', newline ='')
            with file:
                write = csv.writer(file)
                write.writerow(captured_plants[-1])

    if offline_plants:
        filename = get_variable_name(plant_list)
        file2 = open(os.path.join(cwd,f"{folder_name}",f"{filename} Offline Plants.csv"), 'w', newline ='')
        with file2:
            write = csv.writer(file2)
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
