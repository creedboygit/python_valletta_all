import os
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"

driver.get(url=url)
# time.sleep(20)

# //*[@id="loginForm"]/div/div[1]/div/label/input

# Login
id = os.getenv("INSTA_ID")
# pw = getpass.getpass("비밀번호를 입력해주세요. >>> ")
pw = os.getenv("INSTA_PW")

time.sleep(1)

xpath_id = '//*[@id="loginForm"]/div/div[1]/div/label/input'
xpath_pw = '//*[@id="loginForm"]/div/div[2]/div/label/input'

input_id = driver.find_element(By.XPATH, xpath_id)
input_id.send_keys(id)

input_pw = driver.find_element(By.XPATH, xpath_pw)
input_pw.send_keys(pw)

time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

time.sleep(4)

# Hashtag Search
hashtag = "고양이"
# url = "https://www.instagram.com/explore/tags/고양이"
url = f"https://www.instagram.com/explore/tags/{hashtag}"
driver.get(url=url)

time.sleep(5)
print("======= driver.page_source: " + str(driver.page_source))

time.sleep(20)
