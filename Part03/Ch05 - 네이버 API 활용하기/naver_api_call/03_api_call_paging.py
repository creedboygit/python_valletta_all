import requests


def call_api(keyword, start=1, display=100):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url,
                       headers={"X-Naver-Client-Id": "MKbg5ZHY3dMQtloRuNdu", "X-Naver-Client-Secret": "GwIkrgP1g2"})

    r = res.json()
    return r


def get_paging_call(keyword, quantity):
    if quantity > 1100:
        # quantity = 1100
        exit("최대 요청할 수 있는 건수는 100건입니다.")

    repeat = quantity // 100
    result = []
    for i in range(repeat):
        start = i * 100 + 1

        if start > 1000:
            start = 1000

        print(f"{i + 1}번 반복합니다. start: {start}")
        r = call_api(keyword, start=start, display=100)
        result += r['items']
    return result


if __name__ == '__main__':
    # r = call_api("강남병원", 1, 1)
    #
    # for item in r['items']:
    #     print(item)

    r = get_paging_call("강남역맛집", 1100)
    print(len(r))
