# 22-01-28
# 멜론 로그인 후 마이페이지에서 각 월에 많이 들은 곡 리스트 크롤링
from selenium import webdriver
from selenium.webdriver.common.by import By
import my_info
import time
import csv
from datetime import datetime

driver = webdriver.Chrome(my_info.my_path+'/Selenium/chromedriver.exe')
url = 'https://member.melon.com/muid/web/login/login_informM.htm'
driver.get(url)

# 로그인
driver.find_element(By.ID, "id").send_keys(my_info.id_m)
driver.find_element(By.ID, "pwd").send_keys(my_info.pw_m)
driver.find_element(By.ID, "btnLogin").click()

url_mypage = 'https://www.melon.com/mymusic/top/mymusictopmanysong_list.htm?memberKey='
driver.get(url_mypage+my_info.memberKey)
# time.sleep(2)

# 리스트를 csv로 저장
def save_to_file(lists):
    print("save to file")
    dt_today = datetime.today()
    today = dt_today.strftime('%Y-%m-%d_%H-%M-%S')
    file = open(my_info.my_path + f"/Selenium/Monthly_Top_10_{today}.csv",
                mode="w", newline="", encoding='utf-8-sig')

    writer = csv.writer(file)
    writer.writerow(["year", "month", "title", "artist", "rank"])

    for list_y in lists:
        for list_m in list_y:
            for song in list_m:
                writer.writerow(song)
    return True

# 해당 월의 1st 노래만 가져오기
def get_monthly_1st_song(month, year):
    monthly_1st_songs = []
    time.sleep(0.5)
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    try:
        monthly_1st_song = []
        tleft = trs[0].find_element(By.CLASS_NAME, "t_left")
        title = tleft.find_elements(By.TAG_NAME, "a")[1].text
        artist = trs[0].find_element(By.ID, "artistName").text
        print(title)
        print()
        monthly_1st_song.append(year)
        monthly_1st_song.append(month)
        monthly_1st_song.append(title)
        monthly_1st_song.append(artist)
    except:
        print("해당 월에 들은 노래가 없습니다.")
        print()
        monthly_1st_song.append(year)
        monthly_1st_song.append(month)
        monthly_1st_song.append("None")

    monthly_1st_songs.append(monthly_1st_song)
    return monthly_1st_songs

# 선택한 월의 TOP 10 목록 가져오기
def get_monthly_top_songs(month, year, num):
    monthly_top_songs = []
    time.sleep(0.5)
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    cnt = 0

    for i in range(num):
        try:
            msl = []
            rank = trs[i].find_element(By.CLASS_NAME, "no").text
            tleft = trs[i].find_element(By.CLASS_NAME, "t_left")
            title = tleft.find_elements(By.TAG_NAME, "a")[1].text
            artist = trs[i].find_element(By.ID, "artistName").text
            msl.append(year)
            msl.append(month)
            msl.append(title)
            if i==0:
                print(title)
                print()
            msl.append(artist)
            msl.append(rank)
            cnt += 1
        except:
            break

        monthly_top_songs.append(msl)

    if cnt==0:
        print("곡 없음 :: "+str(cnt))
        print()
        monthly_top_songs.append([year, month, "None"])

    return monthly_top_songs

# 1년(12달) 클릭 후 크롤링
def get_one_year(year):
    lists = []
    for i in range(12):
        month_calendar = driver.find_element(By.CLASS_NAME, "month_calendar")
        month_btn = month_calendar.find_elements(By.CLASS_NAME, "btn") # 12개
        month_btn[i].click()
        print(str(i+1)+"월")
        month = i+1
        # 선택한 월의 곡 목록 가져오기
        lists.append(get_monthly_top_songs(month, year, 10))
        # lists.append(get_monthly_1st_song(month, year))
        driver.find_element(By.CLASS_NAME, "d_btn_calenadar").click()
    return lists



# 월별보기 클릭
calendar = driver.find_element(By.CLASS_NAME, "d_btn_calenadar")
calendar.click()

def check_year():
    my_list = []
    year = driver.find_element(By.CLASS_NAME, "date").text
    while(True):
        if year == "2015":
            print("종료")
            break
        elif year == "2022":
            print(year + "::going to previous year")
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "btn_round.small.pre").click()
            year = driver.find_element(By.CLASS_NAME, "date").text
            continue
        else:
            print(year)

            # 1~12월 곡 리스트 가져오는 함수
            my_list.append(get_one_year(year))
            time.sleep(1)

            # 이전 년도로 이동
            driver.find_element(By.CLASS_NAME, "btn_round.small.pre").click()
            year = driver.find_element(By.CLASS_NAME, "date").text

    print(my_list)

    return my_list

mylist = check_year()
save_to_file(mylist)


driver.quit()
