from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# SetUp del driver para Firefox

options = Options()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

user_email = "franz_val@hotmail.com"
psswd = "losbuddies1123581321"

url = "https://www.netflix.com.mx/login"

time.sleep(3)

# Utilizamos el XPath para localizar los elementos

email_field = driver.find_element(By.XPATH, '//*[@id=":rc:"]')
email_field.send_keys(user_email)

psswd_field = driver.find_element(By.XPATH, '//*[@id=":rf:"]')
psswd_field.send_keys(psswd)

submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/button[1]')
submit_button.click()

time.sleep(5)

if "browse" in driver.current_url():
    print("¡Inicio de sesión exitoso!")
else:
    print("Inicio de sesión fallido")


driver.quit()