import pandas as pd
import requests
from bs4 import BeautifulSoup


def crawl(code):
    # url = "https://finance.naver.com/item/main.naver?code=005930"
    url = f"https://finance.naver.com/item/main.naver?code={code}"

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
    # print(price)
    # print(price.text)

    # print("======= price: " + str(price))

    h_company = bs4.find("div", {"class": "h_company"})
    # print("h_company: " + str(h_company.a))
    # print("h_company: " + str(h_company.find("a")))
    # print("h_company: " + str(h_company.find("a").text))
    # print("h_company: " + str(h_company.a.text))

    name = h_company.a.text

    # print("======= name: " + str(name))

    div_description = h_company.find("div", {"class": "description"})
    # print("div_description: " + str(div_description))

    code = div_description.span.text

    # print("======= code: " + str(code))

    table_no_info = bs4.find("table", {"class": "no_info"})
    tds = table_no_info.tr.find_all("td")

    # print("======= tds: " + str(tds))

    volume = tds[2].find("span", {"class": "blind"}).text

    # print("======= volume: " + str(volume))

    dic = {"price": price, "name": name, "code": code, "volume": volume}

    # print("======= dic: " + str(dic))

    return dic


dic = crawl('005930')

# print("======= dic: " + str(dic))

dic2 = crawl('251340')

# print("======= dic: " + str(dic))

codes = ["035720", "005930", "051910", "000660"]

r = []

for code in codes:
    dic2 = crawl(code)
    r.append(dic2)
    # print("======= dic: " + str(dic))
print("======= r: " + str(r))

df = pd.DataFrame(r)
print("======= df: " + str(df))
df.to_excel("prices.xlsx")
