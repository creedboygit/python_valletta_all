from bs4 import BeautifulSoup

f = open("local_info.html", encoding="utf-8")
page_string = f.read()
# print(page_string)
soup = BeautifulSoup(page_string, "html.parser")
# print(soup)
table = soup.find("table", {"class": "table01 fz15"})
# print(table)
trs = table.find("tbody").find_all("tr")
# print("======= trs: " + str(trs))
# print("======= len(trs): " + str(len(trs)))
# for tr in trs:
#     print(tr)
#     print("---------")

tr = trs[2]
# print(tr)

# ths = tr.find_all("th")
tds = tr.find_all("td")

# print(tds)

sido = tds[0].text
print(sido)

region = tds[1].text
print(region)

# print(tds[5].text)

민간공고대수 = tds[5]
접수대수 = tds[6]
출고대수 = tds[7]
출고잔여대수 = tds[8]

print(민간공고대수)
print(접수대수)
print(출고대수)
print(출고잔여대수)
