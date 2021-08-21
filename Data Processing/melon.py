import requests
from bs4 import BeautifulSoup
import csv
from my_info import my_path

URL = "https://www.melon.com/search/song/index.htm?q=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form"
URL_SONGID = "https://www.melon.com/song/detail.htm?songId="
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


# 각 row에서 song id, 곡 제목, 앨범명 가져오기
def get_song_info(tr):
  song_id = tr.find("input", {"class":"input_check"}).get("value")
  song_id = int(song_id)
  title = tr.find("a", {"class":"fc_gray"}).string
  ellipsis = tr.find_all("div", {"class":"ellipsis"})[2]
  album = ellipsis.find("a", {"class":"fc_mgray"}).string
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


# 페이지에 있는 song id 전부 가져오기
def get_song_id():
  req = requests.get(URL, headers=HEADERS)
  soup = BeautifulSoup(req.text, "html.parser")
  results = soup.find_all("input", {"class": "input_check"})

  song_id_set = []
  for result in results[1:]:
    song_id = result.get('value')
    song_id_set.append(song_id)

  return song_id_set


# 가져온 song id로 xhr link 만들기
def make_xhr_link(song_id_set):

  xhr = "https://www.melon.com/commonlike/getSongLike.json?contsIds="
  xhr = xhr + song_id_set[0]

  for sid in song_id_set[1:]:
    xhr = xhr + '%2C' + sid

  return xhr


def save_to_file(songs):
  file = open(my_path+"/Data Processing/songs.csv", mode="w", newline="", encoding='utf-8-sig')
  writer = csv.writer(file)
  writer.writerow(["song_id", "title", "album", "likes"])
  for song in songs:
    writer.writerow(list(song.values()))
  return



# xhr에서 song_id, 좋아요수 두 가지로, 딕셔너리 리스트 만들기
xhr_link = make_xhr_link(get_song_id())
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

# print(len(d_list))

s_list = get_song_list()

# song id로 정렬
songs = sorted(s_list, key=lambda k:k['song_id'], reverse=True)
xhr = sorted(d_list, key=lambda k:k['song_id'], reverse=True)

# xhr에 있는 likes의 value를 songs의 likes에 업데이트
# 딕셔너리 값 수정
for i in range(50):
  # songs[i].append({'likes':likes_cnt[i]})
  songs[i].update(likes=xhr[i]['likes'])

# 좋아요 많은 순으로 정렬
songs_sorted = sorted(songs, key=lambda k:k['likes'], reverse=True)

# csv로 저장
save_to_file(songs_sorted)
