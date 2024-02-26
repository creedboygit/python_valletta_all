from urllib.request import Request, urlopen

import requests


class NaverSearchApi():
    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=100):
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url,
                           headers={"X-Naver-Client-Id": "MKbg5ZHY3dMQtloRuNdu", "X-Naver-Client-Secret": "GwIkrgP1g2"})

        r = res.json()
        return r

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity = 1100
            exit("최대 요청할 수 있는 건수는 100건입니다.")

        repeat = quantity // 100
        display = 100

        if quantity < 100:
            display = quantity
            repeat = 1

        result = []
        for i in range(repeat):
            start = i * 100 + 1

            if start > 1000:
                start = 1000

            print(f"{i + 1}번 반복합니다. start: {start}")
            r = self.call_api(keyword, start=start, display=display)
            # print("======= r: " + str(r))

            result += r['items']
        return result

    def save_images(self, r):
        cnt = 0
        for img in r:
            image_url = img['link']
            image_byte = Request(image_url, headers={'User-Agent': 'Mozzila/5.0'})
            f = open(f'{cnt}.jpg', 'wb')
            f.write(urlopen(image_byte).read())
            f.close()
            cnt += 1

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        # return self.call_api(keyword)
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

    def image(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/image"
        return self.get_paging_call(keyword, quantity)


if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    # r = naver_search_api.call_api("잠실역 맛집")
    # r1 = naver_search_api.blog("잠실역 맛집", 1000)
    # r2 = naver_search_api.news("잠실역 맛집", 1000)
    # r3 = naver_search_api.webkr("잠실역 맛집", 20)
    r4 = naver_search_api.image("잠실역 맛집", 100)

    # print(r1[0]['title'])
    # print(r2[0])
    # print(r3[0])
    # print("======= r3: " + str(r3))
    # print("======= len(r3): " + str(len(r3)))
    print("======= r4: " + str(r4))

    naver_search_api.save_images(r4)
