import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.naver?code=005930"

res = requests.get(url)

# print(res)

# print(res.text)

bs4 = BeautifulSoup(res.text, "html.parser")
# print(bs4)

div_today = bs4.find("div", {"class": "today"})
# print(div_today)

em = div_today.find("em")
# print(em)

# price = em.find("span")
price = em.find("span", {"class": "blind"}).text
print(price)
# print(price.text)
