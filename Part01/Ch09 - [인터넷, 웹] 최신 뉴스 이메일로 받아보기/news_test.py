# news.naver.com -> title crawling
# news.naver.com -> title, content crawling
# news.naver.com -> title, content, image crawling

# 1. title crawling
import requests
from bs4 import BeautifulSoup

def crawling_title():
    """
    Crawls the titles from the given URL and returns a list of titles that are not empty.
    """
    url = "https://news.naver.com"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Select all elements with class "cc_text_item" and filter out empty titles
    titles = soup.select("div.cc_text_list.cc_text_item")
    #

    print(titles)

    title_list = [title.get_text().strip() for title in titles if title.get_text().strip()]
    return title_list

crawling_title()
