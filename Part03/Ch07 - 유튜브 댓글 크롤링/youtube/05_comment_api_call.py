import pprint

from googleapiclient.discovery import build
import os


class YoutubeApi:
    def __init__(self, api_key):
        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def youtube_search(self, query):
        search_response = self.youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResults=10
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


if __name__ == "__main__":
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)
    video_ids = api.youtube_search("슈카월드")
    # video_id = ("exgO1LFl9x8", "3VRw7UVJPQk", "8mkvyl8_4lk")
    # video_id = "rJE6bhVUNhk,exgO1LFl9x8,8mkvyl8_4lk"
    r_video = api.video(video_ids)
    for item in r_video:
        print(item)
