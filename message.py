from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import os
import telepot

telegram_bot = telepot.Bot(token="5320210497:AAFh8g9HJOxG4Om8KpqM5DZMO5f3WFQzMFQ")

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
chromedriver = "/usr/bin/chromedriver"

user_link = "https://www.messenger.com/t/100079285037181"

facebook_bot_username = 'lorcaphan@gmail.com'
facebook_bot_password = 'Longphan0612'

def messenger():
    
    driver = webdriver.Chrome(chromedriver, 
                              chrome_options=options)

    driver.get("https://www.messenger.com/login/")

    time.sleep(2)

    username = driver.find_element_by_id('email')
    username.send_keys(facebook_bot_username)

    password = driver.find_element_by_id('pass')
    password.send_keys(facebook_bot_password)

    login = driver.find_element_by_id('loginbutton')
    login.click()
    
    driver.get(user_link)
    
    time.sleep(8)
    
    # pyautogui.write("[ALERT] Detected someone in the frame!")
    
    # time.sleep(2)

    # pyautogui.press('enter')
    
    
    os.system(f"xclip -selection clipboard -t image/png -i {'~/RPI-People-Detection' + '/image.png'}")
    
    pyautogui.hotkey('ctrl', 'v')
    
    time.sleep(5)

    pyautogui.press('enter')
    
    time.sleep(2)
    
def telegram():
    
    # telegram_bot.sendMessage(chat_id="1921540131",
#                 text="[ALERT] Detected someone in the frame!")

    telegram_bot.sendPhoto(chat_id="1921540131",
                photo=open("image.png", "rb"))


