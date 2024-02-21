import requests

# requests 는 Http Request(요청)을 보내주는 라이브러리

url = "https://finance.naver.com/item/main.naver?code=005930"
get = requests.get(url)

print(get)
