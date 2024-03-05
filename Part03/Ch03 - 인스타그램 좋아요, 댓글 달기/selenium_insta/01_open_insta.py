import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"

driver.get(url=url)
# time.sleep(20)

# //*[@id="loginForm"]/div/div[1]/div/label/input

xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
