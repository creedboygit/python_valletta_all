import argparse
import logging
import os
import platform
import psutil

import requests
import schedule
from bs4 import BeautifulSoup

# 로거 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 형식 지정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log 파일 생성
file_handler = logging.FileHandler('output.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 네이버 뉴스 URL
url1 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=100'
url2 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=101'
url3 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=102'
url4 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=103'
url5 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=104'
url6 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'


def print_system_info():
    logger.info(f'''
        OS : {platform.system()}
        OS VERSION : {platform.version()}
        Process Information : {platform.processor()}
        Process Architecture : {platform.machine()}
        CPU Cores : {os.cpu_count()}
        RAM Size : {str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "(GB)"}
    ''')


def web_crawler(url):
    # 헤더 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    # 서버 응답 확인
    response = requests.get(url, headers=headers)

    # BeautifulSoup 객체 생성
    beautifulSoup = BeautifulSoup(response.content, "html.parser")

    # 페이지 제목 크롤링
    print(beautifulSoup.title.string)

    # 기사 제목 크롤링
    # print(beautifulSoup.find("ul", attrs={"class": "type06_headline"}).get_text())


def main(cpu=3):
    from multiprocessing import Pool
    import time

    url_list = [url1, url2, url3, url4, url5, url6]

    logger.info(f'''멀티 프로세스가 시작됩니다.''')
    start_time = time.time()

    pool = Pool(processes=cpu)  # N개 CPU 코어를 사용
    result = pool.map(web_crawler, url_list)  # 각 URL에 웹 크롤러 할당

    pool.close()  # 풀링 종료
    pool.join()  # 결과 합치기

    logger.info(f'''멀티 프로세스가 종료되었습니다.''')
    logger.info("--- %s second ---" % (time.time() - start_time))


if __name__ == "__main__":

    ''' 입력 매개변수 설정'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', type=int, default=3, help="멀티프로세스 CPU 수")
    parser.add_argument('--run_interval', type=int, default=5, help="웹 크롤러 실행 주기(초)")
    args = parser.parse_args()  # 매개변수 파싱
    cpu = args.cpu
    interval = args.run_interval

    logger.info(f'''
        CPU 사용 : {cpu} 코어
        프로그램 실행 주기 : {interval} 초
    ''')

    # N초에 한번씩 메인 함수 실행
    job = schedule.every(interval).seconds.do(main, cpu)  # 이벤트 등록

    # 스케줄러 실행
    count = 0

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    #
    #     count += 1
    #
    #     if count > 5:
    #         schedule.cancel_job(job)
    #         print('스케줄러가 종료되었습니다')
    #         break

    while True:
        schedule.run_pending()
