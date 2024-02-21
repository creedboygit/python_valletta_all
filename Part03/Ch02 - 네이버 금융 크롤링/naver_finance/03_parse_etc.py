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
# print(price)
# print(price.text)

h_company = bs4.find("div", {"class": "h_company"})
print("h_company: " + str(h_company.a))
print("h_company: " + str(h_company.find("a")))
print("h_company: " + str(h_company.find("a").text))
print("h_company: " + str(h_company.a.text))

name = h_company.a.text
print("name: " + str(name))

div_description = h_company.find("div", {"class": "description"})
# print("div_description: " + str(div_description))

code = div_description.span.text

print("\n==== START : code ====\n" + "code: " + str(code) + "\n==== END : code ====\n")

table_no_info = bs4.find("table", {"class": "no_info"})
tds = table_no_info.tr.find_all("td")

print("\n==== START : tds ====\n" + "tds: " + str(tds) + "\n==== END : tds ====\n")

volume = tds[2].find("span", {"class": "blind"}).text

print("\n==== START : volume ====\n" + "volume: " + str(volume) + "\n==== END : volume ====\n")

dic = {"price": price, "name": name, "code": code, "volume": volume}

print("\n==== START : dic ====\n" + "dic: " + str(dic) + "\n==== END : dic ====\n")
