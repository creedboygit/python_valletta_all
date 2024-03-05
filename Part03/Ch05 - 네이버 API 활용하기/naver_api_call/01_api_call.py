import json

import requests

url = "https://openapi.naver.com/v1/search/blog.json?query=강남맛집&start=101&display=100"
res = requests.get(url, headers={"X-Naver-Client-Id": "MKbg5ZHY3dMQtloRuNdu", "X-Naver-Client-Secret": "GwIkrgP1g2"})

print("======= res: " + str(res.text))
# print("======= res: " + str(res.json()))

res_temp = json.loads(res.text)
# print("======= res_temp: " + str(res_temp))
# print(type(res_temp))
# print(json.dumps(res_temp, indent=4, sort_keys=True))

print(json.dumps(res.json(), indent=4, sort_keys=True))

r = res.json()
print(r['total'])
print(r['items'])
# print(len(r['items']))

print("======= len(r['items']): " + str(len(r['items'])))

for item in r['items']:
    print(item)
