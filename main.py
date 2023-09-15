from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import fast_colorthief
from PIL import ImageGrab
from PIL import ImageTk
from skimage import io
import tkinter as tk
import pyautogui
import math
import csv
import time
import os
from config import *

# Function to capture screenshot
def capture_dvr(plant_list,plant,delay):
    global captured_plants
    global offline_plants
    global blacklist
    if plant_list[plant]["gui"] != "ever" and plant not in blacklist:

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        try:
            driver.set_page_load_timeout(45)
            driver.get(plant_list[plant]["url"])
        except:
            offline_plants.append(plant)
            file = open(os.path.join(cwd,f"{folder_name}","Offline Plants.csv"), 'a', newline ='')
            with file:
                write = csv.writer(file)
                write.writerow([plant])
            driver.quit()
            return

        driver.maximize_window()

        time.sleep(delay)

        try:
            username = driver.find_element(By.XPATH, '//input[@placeholder="User Name"]')
            username.send_keys(plant_list[plant]["user"])
            password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
            password.send_keys(plant_list[plant]["password"])
            driver.find_element(By.XPATH, "//button").click()
        except:
            pass

        time.sleep(delay+5)
        
        try:
            if plant_list[plant]["gui"] == "hik-1":
                driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]/i[contains(@class, 'icon-playall')]").click()
            elif plant_list[plant]["gui"] == "hik-2":
                driver.find_element(By.XPATH, "//button[@title='Start All Live View']").click()
        except:
            pass

        time.sleep(delay)

        ss_region = (0,0,1920,1080)
        ss_img = ImageGrab.grab(ss_region)
        ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))

        if plant not in offline_plants:
            check_cameras(plant_list[plant]["grid"],plant_list[plant]["cams"],plant_list,plant)

        driver.quit()

    elif plant_list[plant]["gui"] != "ever" and plant in blacklist:
        ie_options = webdriver.IeOptions()
        ie_options.attach_to_edge_chrome = False
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()),options=ie_options)          
        try:
            driver.set_page_load_timeout(delay-5)
            driver.get(plant_list[plant]["url"])
        except:
            driver.maximize_window()
            time.sleep(delay)
            pyautogui.moveTo(1366,574,duration=1)
            pyautogui.click()
            pyautogui.typewrite(plant_list[plant]["user"],interval=0.1)
            pyautogui.moveTo(1366,627,duration=1)
            pyautogui.click()
            pyautogui.typewrite(plant_list[plant]["password"],interval=0.1)
            pyautogui.moveTo(1366,700,duration=1)
            pyautogui.click()
            
            time.sleep(delay+5)

            if plant_list[plant]["gui"] == "hik-1":
                try:
                    driver.find_element(By.XPATH, "//button[contains(@class, 'btn')]/i[contains(@class, 'icon-playall')]").click()
                except:
                    time.sleep(delay-5)
                    ss_region = (0,0,1920,1080)
                    ss_img = ImageGrab.grab(ss_region)
                    ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))
                    color_palette = fast_colorthief.get_palette(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"),2,2)
                    if color_palette[0][0] > 220 and color_palette[0][1] > 220 and color_palette[0][2] > 220:
                        offline_plants.append(plant)
                        file = open(os.path.join(cwd,f"{folder_name}","Offline Plants.csv"), 'a', newline ="")
                        with file:
                            write = csv.writer(file)
                            write.writerow([plant])
                    if plant not in offline_plants:
                        check_cameras(plant_list[plant]["grid"],plant_list[plant]["cams"],plant_list,plant)
                    pyautogui.moveTo(1900,30,duration=0.5)
                    pyautogui.click()                     
            elif plant_list[plant]["gui"] == "hik-2":
                try:
                    driver.find_element(By.XPATH, "//button[@title='Start All Live View']").click()
                except:
                    time.sleep(delay-5)
                    ss_region = (0,0,1920,1080)
                    ss_img = ImageGrab.grab(ss_region)
                    ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))
                    color_palette = fast_colorthief.get_palette(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"),2,2)
                    if color_palette[0][0] > 220 and color_palette[0][1] > 220 and color_palette[0][2] > 220:
                        file = open(os.path.join(cwd,f"{folder_name}","Offline Plants.csv"), 'a', newline ='')
                        with file:
                            write = csv.writer(file)
                            write.writerow([plant])
                    check_cameras(plant_list[plant]["grid"],plant_list[plant]["cams"],plant_list,plant)
                    pyautogui.moveTo(1900,30,duration=0.5)
                    pyautogui.click()                   
    else:
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        try:
            driver.set_page_load_timeout(delay-5)
            driver.get(plant_list[plant]["url"])
        except:
            pyautogui.moveTo(550,700,duration=2)
            pyautogui.click()
            time.sleep(delay-5)
            driver.maximize_window()
            time.sleep(delay-3)
            ss_region = (0,0,1920,1080)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"))
            color_palette = fast_colorthief.get_palette(os.path.join(cwd,f"{folder_name}",f"{plant}.jpg"),2,2)
            if color_palette[0][0] > 220 and color_palette[0][1] > 220 and color_palette[0][2] > 220:
                offline_plants.append(plant)
                file = open(os.path.join(cwd,f"{folder_name}","Offline Plants.csv"), 'a', newline ="")
                with file:
                    write = csv.writer(file)
                    write.writerow([plant])
            if plant not in offline_plants:
                check_cameras(plant_list[plant]["grid"],plant_list[plant]["cams"],plant_list,plant)
            driver.quit()       


# Function to run capture_dvr for all plants in plant_list
def run_capture_dvr(plant_list):
    global field
    global captured_plants
    global delay

    if type(plant_list) is str:
        try:
            plant_list = {plant_list:ALL_PLANTS[plant_list]}
        except KeyError:
            print("Choose a plant first")

    for plant in plant_list:
        if plant not in captured_plants and [plant] not in captured_plants:
            if plant in ultra_slow_plants:
                capture_dvr(plant_list,plant,6*delay)           
            elif plant in slow_plants:
                capture_dvr(plant_list,plant,2*delay)
            elif plant in very_slow_plants:
                capture_dvr(plant_list,plant,4*delay)
            else:
                capture_dvr(plant_list,plant,delay)
            captured_plants.append([plant])
            file2 = open(os.path.join(cwd,f"{folder_name}","Captured Plants.csv"), 'a', newline ='')
            with file2:
                write = csv.writer(file2)
                write.writerow(captured_plants[-1])


#Function to check which cameras don't work for specific plant
def check_cameras(grid,cams_num,plant_list,plant):
    if plant_list[plant]["type"] == "hik-1":
        start = (250,200)
        finish = (1645,940)
    elif plant_list[plant]["type"] == "hik-2":
        start = (325,179)
        finish = (1595,901)
    elif plant_list[plant]["type"] == "hik-3":
        start = (251,351)
        finish = (1645,942)
    elif plant_list[plant]["type"] == "ever":
        start = (627,377)
        finish = (1553,953)
    width = (finish[0]-start[0])/math.sqrt(grid)
    height = (finish[1]-start[1])/math.sqrt(grid)
    off_cameras = ""
    for i in range(cams_num):
        y = int(i//math.sqrt(grid))
        x = i - int((y*math.sqrt(grid)))
        scrstart_x = int(start[0] + width * x)
        scrstart_y = int(start[1] + height * y)
        ss_region = (scrstart_x, scrstart_y, scrstart_x + width, scrstart_y + height)
        ss_img = ImageGrab.grab(ss_region)
        ss_img.save(os.path.join(cwd,f"{folder_name}",f"{plant}_Cam{i+1}.jpg"))
        time.sleep(1)
        color_palette = io.imread(os.path.join(cwd,f"{folder_name}",f"{plant}_Cam{i+1}.jpg"))[:, :, :]
        average = color_palette.mean(axis=0).mean(axis=0)
        if plant_list[plant]["type"] == "hik-1" or plant_list[plant]["type"] == "hik-2" or plant_list[plant]["type"] == "hik-3":
            if average[0] < 60 and average[1] < 60 and average[2] < 60:
                off_cameras += f" Cam{i+1}"
        else:
            if (average[0] < 60 and average[1] < 60 and average[2] > 220) or (average[0] < 60 and average[1] < 60 and average[2] > 60):
                off_cameras += f" Cam{i+1}"    
        os.remove(os.path.join(cwd,f"{folder_name}",f"{plant}_Cam{i+1}.jpg"))
    if off_cameras != "":
        file = open(os.path.join(cwd,f"{folder_name}","Cameras Status.csv"), 'a', newline ="")
        with file:
            write = csv.writer(file)
            write.writerow([plant+":"+off_cameras+" not working"])
        
os.environ['GH_TOKEN'] = "****************************"

root = tk.Tk()
root.title("DVR Screen Capture")

current_plant = tk.StringVar(root)
current_plant.set("-Choose Plant-")

x = root.winfo_screenwidth()//2-250
y = int(root.winfo_screenheight()*0.1)
root.geometry('540x750+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=540, height=750, bg=bg_color)
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

button7 = tk.Button(
    frame1,
    text="PLANT GROUP 7",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_6))

button8 = tk.Button(
    frame1,
    text="PLANT GROUP 7",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(PLANT_GROUP_6))

button9 = tk.Button(
    frame1,
    text="CAPTURE PLANT",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#4f6457",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(current_plant.get()))

button10 = tk.Button(
    frame1,
    text="CAPTURE ALL",
    height=2,
    width=15,
    font=("TkHeadingFont",12),
    bg="#4f6457",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:run_capture_dvr(ALL_PLANTS))

button1.place(x=65,y=200)
button2.place(x=330,y=200)
button3.place(x=65,y=280)
button4.place(x=330,y=280)
button5.place(x=65,y=360)
button6.place(x=330,y=360)
button7.place(x=65,y=440)
button8.place(x=330,y=440)
button9.place(x=65,y=630)
button10.place(x=65,y=550)

menu = tk.OptionMenu(frame1, current_plant, *ALL_PLANTS_LIST)
menu.config(bg="#4f6457",fg="white",activebackground="#badee2",activeforeground="black",font=("TkHeadingFont",12),highlightthickness=0)
menu.place(x=245,y=645)

root.mainloop()
