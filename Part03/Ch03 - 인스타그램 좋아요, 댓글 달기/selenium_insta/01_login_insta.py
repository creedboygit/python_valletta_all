from selenium import webdriver
import chromedriver_autoinstaller
import time

from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"

driver.get(url=url)
# time.sleep(20)

# //*[@id="loginForm"]/div/div[1]/div/label/input

xpath_id = '//*[@id="loginForm"]/div/div[1]/div/label/input'

input_id = driver.find_element(By.XPATH, xpath_id)
