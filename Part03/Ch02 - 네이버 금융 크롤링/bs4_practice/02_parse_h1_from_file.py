from bs4 import BeautifulSoup

f = open("..\\tag_practice\\01_h1_tag.html", encoding="utf-8")

f_str = f.read()
print(f_str)

bs4 = BeautifulSoup(f_str, "html.parser")

print(bs4)

h1 = bs4.find("h1")
p = bs4.find("p")
h2 = bs4.find("h2")

print(h1)
print(p)
print(h2)

print()

print(h1.text)
print(p.text)
print(h2.text)

# .string
# .string 태그 하위의 문자열을 객체화한다.
# 문자열이 없으면 None을 반환한다.
# 스트링만 리스트로 추출함.
# 줄바꿈, 공백 등 필요없는 것들에 제거한 스트링 리스트를 리턴함.


# .text
# 하위 자식태그의 텍스트까지 문자열로 반환한다.
# 일반적으로 텍스트 부분만 모두 추출함.
# 하나의 스트링을 만들어 리턴함.
