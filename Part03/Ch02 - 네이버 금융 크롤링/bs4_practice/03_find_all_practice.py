from bs4 import BeautifulSoup

f = open("..\\tag_practice\\02_ul_li.html", encoding="utf-8")
bs4 = BeautifulSoup(f.read(), "html.parser")
print(bs4)

ul = bs4.find("ul")
print(ul)

lis = ul.find("li")
print(lis)

lis2 = ul.find_all("li")
print(lis2)

print()

print("type: " + str(type(lis2)))

print()

for li in lis2:
    print(li.text)
