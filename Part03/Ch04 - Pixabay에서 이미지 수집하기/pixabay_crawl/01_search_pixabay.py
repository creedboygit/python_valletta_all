import chromedriver_autoinstaller
from selenium import webdriver
from time import sleep
from urllib.request import Request, urlopen

from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# url = "https://pixabay.com/ko/"
url = "https://pixabay.com/ko/images/search/고양이/"
driver.get(url=url)

image_xpath = "/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/a/img"
image_url = driver.find_element(By.XPATH, image_xpath).get_attribute('src')

print("======= image_url: " + str(image_url))

image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
f = open("cat.jpg", "wb")
f.write(urlopen(image_byte).read())
f.close()

# sleep(30)
