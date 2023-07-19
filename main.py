import time
import csv
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get('https://twitter.com/lautidev_/status/1679273373426221057')

authToken = input("ingrese authToken")

driver.add_cookie({'name': 'auth_token', 'value': authToken, 'domain': '.twitter.com'})
# Actualiza la página para cargar la sesión con la cookie
driver.refresh()
driver.maximize_window()
driver.implicitly_wait(5)

input("sape")

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) # Espera a que se carguen las respuestas adicionales
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            botonVerMas=driver.find_element(By.XPATH, "//span[contains(text(),'Show more replies')]/ancestor::*[position()=3]")
            if not botonVerMas.is_displayed():
             # If the element is not visible, scroll to it
                driver.execute_script("arguments[0].scrollIntoView();", botonVerMas)
            # wait = WebDriverWait(driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.ID, "my_element_id")))
            # botonVerMas.click()
        except NoSuchElementException:
            break
    last_height = new_height

