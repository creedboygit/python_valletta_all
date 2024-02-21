from bs4 import BeautifulSoup

bs4 = BeautifulSoup("<html><body><h1>안녕하세요</h1></body></html>", "html.parser")

print(bs4)

# .find() .find_all()
print(bs4.find())

h1 = bs4.find("h1")
print(h1.text)
print(h1.string)
