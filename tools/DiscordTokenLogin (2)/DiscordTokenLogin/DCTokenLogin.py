import os, sys, ctypes, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.system('cls')

print("""
  _______    _              _                 _       
 |__   __|  | |            | |               (_)      
    | | ___ | | _____ _ __ | |     ___   __ _ _ _ __  
    | |/ _ \| |/ / _ \ '_ \| |    / _ \ / _` | | '_ \ 
    | | (_) |   <  __/ | | | |___| (_) | (_| | | | | |
    |_|\___/|_|\_\___|_| |_|______\___/ \__, |_|_| |_|
                                         __/ |        
                                        |___/         
""")

token = input('Token: ')
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://discord.com/login')
js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
time.sleep(3)
driver.execute_script(js + f'login("{token}")')
