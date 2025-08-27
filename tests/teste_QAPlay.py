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

#1-
# Acessa site de compra de café
# Escolhe o café "Expresso" e clica nele
# Depois clica em "Cart" para ver quais os cafés que o usuário colocou no carrinho
# Depois finaliza a compra clicando em "Total"
# Após isso irá abrir o campo para digitar o nome e email para que seja eviado o link de pagamento


def compra_cafe():
    driver=webdriver.Chrome(options=options)
    driver.get("https://coffee-cart.app/")

    time.sleep (2)

    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/ul/li[1]').click()

    time.sleep (2)

    driver.find_element(By.XPATH, '//*[@id="app"]/ul/li[2]/a').click()

    time.sleep (2)

    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/button').click()

    time.sleep (2)

    driver.find_element(By.ID, 'name').send_keys("Paulo")

    time.sleep (2)