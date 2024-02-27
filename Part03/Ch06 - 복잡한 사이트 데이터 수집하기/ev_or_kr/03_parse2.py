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

replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]

민간공고대수 = replace_brackets(tds[5].text)
접수대수 = replace_brackets(tds[6].text)
출고대수 = replace_brackets(tds[7].text)
출고잔여대수 = replace_brackets(tds[8].text)

print(민간공고대수)
# print(접수대수)
# print(출고대수)
# print(출고잔여대수)

'''
string1 = "<td>3679<br/> (368)<br/> (0)<br/> (736)<br/> (2575)</td>"
print(
    string1.replace("(", "")
    .replace(")", "")
    .replace("<br/>", "")
    .replace("<td>", "")
    .replace("</td>", "")
    .split(" "))
'''

row = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "우선순위", "value": 1650}
row2 = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "법인및기관", "value": 2500}

print("======= row: " + str(row))
print("======= row2: " + str(row2))
