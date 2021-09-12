# 멜론 페이지에서 BTS TOP 200 곡 가져온 후에, 좋아요 순으로 정렬해서 csv로 저장.
# 21-08-23
# #params 말고 제대로 된 주소 가져오기 성공

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from my_info import my_path

URL = "https://www.melon.com/search/song/index.htm?startIndex=151&pageSize=50&q=%25EB%25B0%25A9%25ED%2583%2584%25EC%2586%258C%25EB%2585%2584%25EB%258B%25A8&sort=hit&section=all&sectionId=&genreDir="

URL_1 = "https://www.melon.com/search/song/index.htm?startIndex="
URL_2 = "&pageSize=50&q=%25EB%25B0%25A9%25ED%2583%2584%25EC%2586%258C%25EB%2585%2584%25EB%258B%25A8&sort=hit&section=all&sectionId=&genreDir="

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def get_song_id():
    req = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(req.text, "html.parser")
    results = soup.find_all("input", {"class": "input_check"})

    song_id_set = []

    for result in results[1:]:
        song_id = result.get('value')
        song_id_set.append(song_id)
    return song_id_set

# 각 row에서 song id, 곡 제목, 앨범명 가져오기
def get_song_info(tr):
    song_id = tr.find("input", {"class": "input_check"}).get("value")
    song_id = int(song_id)
    title = tr.find("a", {"class": "fc_gray"}).string
    print(title)
    # album = tr.find_all("a", {"class":"fc_mgray"})[2].string # 문제생김.. Savage Love는 artist가 여러명이라서 이걸 하면 앨범으로 안넘어가고 아티스트가 담김
    ellipsis = tr.find_all("div", {"class": "ellipsis"})[2]
    album = ellipsis.find("a", {"class": "fc_mgray"}).string
    likes = 0

    return {
        'song_id': song_id,
        'title': title,
        'album': album,
        'likes': likes
    }

# tablerow 가져오고 각 tr마다 get_song_info 호출
def get_song_list():
    req = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(req.text, "html.parser")

    tablerow = soup.find_all("tr")

    songs_info = []

    for tr in tablerow[1:]:
        songs = get_song_info(tr)
        songs_info.append(songs)

    return songs_info


# 페이지 넘기기 (TOP 200이면 4페이지까지 가면 됨)
# def go_next_page():

def update_likes_cnt():
    return

def make_xhr_link(song_id_set):

    xhr = "https://www.melon.com/commonlike/getSongLike.json?contsIds="

    xhr = xhr + song_id_set[0]

    for sid in song_id_set[1:]:
        xhr = xhr + '%2C' + sid
    # print(xhr)
    return xhr

def save_to_file(songs):
    print("save to file")
    dt_today = datetime.today()
    # today = dt_today.strftime('%Y-%m-%d %H:%M:%S')
    today = dt_today.strftime('%m-%d')
    file = open(my_path+f"/Data Processing/Melon_BTS_TOP_200_LIKES_{today}.csv", mode="w", newline="", encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["song_id", "title", "album", "likes"])
    for song in songs:
        writer.writerow(list(song.values()))
    return

# 매개변수: TOP 200 이면 1, 51, 101, 151 4번 호출. 200/50
def extract_all_songs_info(num):
    songs = []
    for page in range(int(num/50)):
        print(f"Scraping Melon: Page: {page}")
        req = requests.get(f"{URL_1}{page*50+1}{URL_2}", headers=HEADERS)
        soup = BeautifulSoup(req.text, "html.parser")
        tablerow = soup.find_all("tr")

        for tr in tablerow[1:]:
            song = get_song_info(tr)
            songs.append(song)

    # 좋아요 수 update
    song_id_set = []
    for song in songs:
        song_id_set.append(str(song['song_id']))

    xhr_link = make_xhr_link(song_id_set)
    req2 = requests.get(xhr_link, headers=HEADERS)
    soup2 = req2.json()
    song_xhr = soup2['contsLike']
    d_list = []
    for x in song_xhr:
        d_list.append(
            {
                'song_id': x['CONTSID'],
                'likes': x['SUMMCNT']
            }
        )
    s_list = songs
    songs = sorted(s_list, key=lambda k: k['song_id'], reverse=True)
    xhr = sorted(d_list, key=lambda k: k['song_id'], reverse=True)
    for i in range(num):
        songs[i].update(likes=xhr[i]['likes'])
        print(f"update: {i}")

    songs_sorted = sorted(songs, key=lambda k:k['likes'], reverse=True)
    return songs_sorted


songs = extract_all_songs_info(200)
print("========================================================================================")
print(songs)
print(len(songs))
for s in songs:
  print(s['likes'], end=' :: ')
  print(s['title'], end=' - ')
  print(s['album'])

save_to_file(songs)
