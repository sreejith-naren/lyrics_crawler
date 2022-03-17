import os
import requests
from bs4 import BeautifulSoup
def get_artists(url):
    ret=[]
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links= tracklists.find_all("a")
    for i in links:
        ret.append((i.text,i['href']))
    return ret
