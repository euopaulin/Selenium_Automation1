import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--no-proxy-server")     # Ignora proxy de sistema
options.add_argument('--proxy-server=') 

driver=webdriver.Chrome(options=options)
driver.get("https://coffee-cart.app/")

time.sleep (2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/ul/li[1]').click()

time.sleep (2)

driver.find_element(By.XPATH, '//*[@id="app"]/ul/li[2]/a').click()

time.sleep (2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/ul/li[2]/div[2]/div/button[2]').click()


time.sleep(20)

driver.quit()