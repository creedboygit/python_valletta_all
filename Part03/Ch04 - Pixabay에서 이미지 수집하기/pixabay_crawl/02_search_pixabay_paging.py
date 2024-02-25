import os.path

import chromedriver_autoinstaller
from selenium import webdriver
from time import sleep
from urllib.request import Request, urlopen

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()

# options.add_argument('headless')
options.add_argument('--disable-gpu')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


def crawl_image(keyword, pages):
    image_urls = []
    for i in range(1, pages + 1):

        # url = "https://pixabay.com/ko/images/search/사과/?pagi=3"
        url = f"https://pixabay.com/ko/images/search/{keyword}/?pagi={pages}"
        driver.get(url=url)

        # class
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'fb-root')))
        sleep(2)

        image_xpath_area = '/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div'
        image_area = driver.find_element(By.XPATH, image_xpath_area)
        image_elements = image_area.find_elements(By.TAG_NAME, "img")

        for i, image_element in enumerate(image_elements):
            # sleep(1)
            image_url = ""

            if image_element.get_attribute("data-lazy") is None:
                image_url = image_element.get_attribute("src")
            elif image_element.get_attribute("data-lazy-src"):
                image_url = image_element.get_attribute("data-lazy-src")
            else:
                image_url = image_element.get_attribute("data-lazy")

            print("======= image_url: " + str(pages) + " - " + str(image_url))

            if image_url != "https://pixabay.com/static/img/blank.gif":
                image_urls.append(image_url)

    return image_urls


def crawl_and_save_image(keyword, pages):
    image_urls = crawl_image(keyword, 3)
    print(len(image_urls))

    # 디렉토리 만들기
    # keyword = "토마토"

    path = keyword

    if not os.path.exists(path):
        os.mkdir(path)

    for i in range(len(image_urls)):
        image_url = image_urls[i]
        image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})

        filename = image_url.split("/")[-1]
        save_path = f"{path}/{filename}"

        # f = open(f".\\images\\cat{i}.jpg", "wb")
        f = open(save_path, "wb")
        f.write(urlopen(image_byte).read())
        f.close()


crawl_and_save_image("토마토", 3)
crawl_and_save_image("강아지", 3)
crawl_and_save_image("포도", 3)
