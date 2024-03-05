import os
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

url = "https://www.instagram.com/"

driver.get(url=url)
# time.sleep(20)

# //*[@id="loginForm"]/div/div[1]/div/label/input

time.sleep(2)


def login(id, pw):
    xpath_id = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    xpath_pw = '//*[@id="loginForm"]/div/div[2]/div/label/input'

    input_id = driver.find_element(By.XPATH, xpath_id)
    input_id.send_keys(id)

    time.sleep(0.4)

    input_pw = driver.find_element(By.XPATH, xpath_pw)
    input_pw.send_keys(pw)

    time.sleep(2)

    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)


def search(hashtag, scroll_times):
    # url = "https://www.instagram.com/explore/tags/고양이"
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(url=url)

    time.sleep(5)
    # print("======= driver.page_source: " + str(driver.page_source))

    # Scroll
    # for _ in range(5):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(7)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def like_comment(nth, comment, repeat=3):
    # click
    row = (nth - 1) // 3 + 1
    col = (nth - 1) % 3 + 1
    # 몇번째 포스트 클릭
    # xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[3]/div[3]'
    xpath = f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[{row}]/div[{col}]'
    driver.find_element(By.XPATH, xpath).click()

    time.sleep(1)

    divs = 7

    for i in range(repeat):
        time.sleep(2)

        # like_xpath = '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div'
        # like_xpath = f'/html/body/div[{divs}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div'
        like_xpath = '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]'
        driver.find_element(By.XPATH, like_xpath).click()

        time.sleep(0.8)

        # comment
        # comment_xpath = f'/html/body/div[{divs}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
        comment_xpath = '//*[@aria-label="댓글 달기..."]'
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)
        time.sleep(0.8)
        driver.find_element(By.XPATH, comment_xpath).send_keys(Keys.ENTER)

        time.sleep(2)

        # 게시 버튼 클릭
        # comment_button_xpath = '//*[@aria-label="게시"]'
        # driver.find_element(By.XPATH, comment_button_xpath).click()
        # driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        '''
        # comment_button_xpath = '//*[@aria-label="게시"]'
        # driver.find_element(By.XPATH, comment_button_xpath).click()
        # driver.find_element(By.XPATH, comment_xpath).send_keys(comment)
        '''

        '''
        # comment
        comment_xpath = f'/html/body/div[{divs}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        time.sleep(0.8)

        # 게시 버튼 클릭
        comment_button_xpath = f'/html/body/div[{divs}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div'
        driver.find_element(By.XPATH, comment_button_xpath).click()
        '''

        time.sleep(1)

        # 다음 게시물 버튼 누르기
        # next_button_xpath = f'/html/body/div[{divs}]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button/div/span'
        next_button_xpath = '//*[@aria-label="다음"]//ancestor :: span[1]'
        driver.find_element(By.XPATH, next_button_xpath).click()

        time.sleep(0.8)


# Login
id = os.getenv("INSTA_ID")
# pw = getpass.getpass("비밀번호를 입력해주세요. >>> ")
pw = os.getenv("INSTA_PW")

login(id, pw)

time.sleep(7)

# Hashtag Search
hashtag = "고양이"
search(hashtag, 1)

# like comment
like_comment(8, "너무 귀엽네요!!", 4)

time.sleep(20)
