import os
import pprint
import re

from googleapiclient.discovery import build


def get_channel_id(url):
    # 유튜브 채널 URL에서 'UC'로 시작하는 채널 ID를 추출하는 정규 표현식
    pattern = r'youtube\.com\/channel\/(UC[-_A-Za-z0-9]{21}[AQgw])'
    match = re.search(pattern, url)

    if match:
        # 정규 표현식에 해당하는 부분을 찾으면, 그 부분을 반환
        return match.group(1)
    else:
        # 채널 ID를 찾지 못하면 None 반환
        return None


def get_video_links(api_key):
    channel_url = "https://www.youtube.com/@code_bob"
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = get_channel_id(channel_url)

    video_links = []
    request = youtube.search().list(part='snippet', channelId=channel_id, maxResults=50, type='video')
    response = request.execute()

    pprint.pprint(response, width=400)

    for item in response['items']:
        video_id = item['id']['videoId']
        video_link = f'https://www.youtube.com/watch?v={video_id}'
        video_links.append({"title": item['snippet']['title'], "link": video_link})

    # pprint.pprint("======= video_links:" + str(video_links), width=400)

    # 결과를 JSON 파일로 저장
    # with open('video_links.json', 'w', encoding='utf-8') as f:
    #     json.dump(video_links, f, indent=4, ensure_ascii=False)
    #
    # print("동영상 목록이 'video_links.json' 파일에 저장되었습니다.")


if __name__ == '__main__':
    api_key = os.getenv("API_KEY")
    # channel_url = input("YouTube 채널 URL을 입력하세요: ")
    get_video_links(api_key)
