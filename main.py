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
from selenium.webdriver.common.action_chains import ActionChains


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
            break
    last_height = new_height

        
try:
    show_more_button = driver.find_element(By.XPATH, '//span[contains(text(), "Show more replies")]/ancestor::*[position()=3]')
    action = ActionChains(driver)
    action.move_to_element(show_more_button).click().perform()

except NoSuchElementException:
    print("no se encontro")


reply_tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')

# for reply_tweet in reply_tweets:
    # username_link = reply_tweet.find_element(By.XPATH, './div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/a')
    # username = username_link.get_attribute('href')
#     print(username)


reply_tweet = reply_tweets[5]
username_link = reply_tweet.find_element(By.XPATH, './div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a')
username = username_link.get_attribute('href')
print(username)
#4f01cabca155ed5c9df029cd0cce13da422d6052