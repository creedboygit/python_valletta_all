import os

import pandas as pd
from googleapiclient.discovery import build


class YoutubeApi:
    def __init__(self, api_key):
        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def video_search_list(self, query, max_results=10):
        search_response = self.youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResults=max_results
        ).execute()

        # print(search_response)

        video_ids = []
        for item in search_response.get("items", []):
            if item['id']['kind'] == "youtube#video":
                # print(item['id']['video_id'])
                video_ids.append(item['id']['videoId'])
        return ",".join(video_ids)

        # for item in search_response.get("items", []):
        # pprint.pprint(item, width=400)
        # pprint.pprint(item)

    def video(self, video_ids):
        # print(video_ids)
        videos_list_response = self.youtube_api.videos().list(
            id=video_ids,
            part="snippet, statistics"
        ).execute()

        # print(videos_list_response)

        # print(videos_list_response.get("items", []))

        r = []
        for item in videos_list_response.get("items", []):
            # pprint.pprint(item)
            # print(item)
            r.append({"video_id": item["id"],
                      "channelTitle": item["snippet"]["channelTitle"],
                      "title": item["snippet"]["title"],
                      "commentCount": item["statistics"]["commentCount"]})
        return r

    def comment(self, video_id, max_cnt):
        comment_list_response = self.youtube_api.commentThreads().list(
            videoId=video_id,
            part="id,replies,snippet",
            maxResults=max_cnt
        ).execute()

        comments = []
        for comment in comment_list_response.get("items", []):
            snippet = comment['snippet']['topLevelComment']['snippet']
            # print(json.dumps(comment))
            # print(json.dumps(snippet))
            # print(snippet['textOriginal'], snippet['authorDisplayName'], sep="-")
            map = {"link": f"https://www.youtube.com/watch?v={snippet['videoId']}",
                   "videoId": snippet['videoId'],
                   "textOriginal": snippet['textOriginal'],
                   "authorDisplayName": snippet['authorDisplayName']}
            # print("======= map:\n" + str(map))
            comments.append(map)

        return comments

    def save_to_excel(self, search_results, filename):
        df = pd.DataFrame(search_results)
        df.to_excel(filename)

    def crawl_comment_by_keyword(self, keyword, video_cnt=5):
        video_ids = self.video_search_list(keyword, video_cnt)
        r_video = self.video(video_ids)
        # print("video_ids: ", r_video)
        l = []
        for video in r_video:
            cnt = int(video['commentCount'])
            if cnt > 100:
                cnt = 100
            comment_list = self.comment(video['video_id'], cnt)
            l += comment_list
        return l


if __name__ == "__main__":
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)
    video_ids = api.video_search_list("슈카월드")
    # video_id = ("exgO1LFl9x8", "3VRw7UVJPQk", "8mkvyl8_4lk")
    # video_id = "rJE6bhVUNhk,exgO1LFl9x8,8mkvyl8_4lk"

    # r_video = api.video(video_ids)
    # for item in r_video:
    #     print(item)

    # comment_results = api.comment('Mxqn95UzQ78', 61)
    # api.save_to_excel(comment_results, "엑셀.xlsx")

    keyword = "핸드크림"

    l = api.crawl_comment_by_keyword(keyword, 10)
    api.save_to_excel(l, f"{keyword}.xlsx")
