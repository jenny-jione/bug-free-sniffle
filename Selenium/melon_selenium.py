# 22-01-28
# 멜론 로그인 후 마이페이지에서 각 월에 많이 들은 곡 리스트 크롤링
from selenium import webdriver
from selenium.webdriver.common.by import By
import my_info
import time
import csv

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


def save_to_file(lists):
    print("save to file")
    file = open(my_info.my_path + f"/Selenium/Monthly_1st_song_2016_2021.csv",
                mode="a", newline="", encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["year", "month", "title"])
    for list in lists:
        writer.writerow(list)
    return True

# 해당 월의 1st 노래만 가져오기
def get_monthly_1st_song(month, year):
    monthly_1st_songs = []
    time.sleep(0.1)
    try:
        monthly_1st_song = []
        tbody = driver.find_element(By.TAG_NAME, "tbody")
        trs = tbody.find_elements(By.TAG_NAME, "tr")
        tleft = trs[0].find_element(By.CLASS_NAME, "t_left")
        title = tleft.find_elements(By.TAG_NAME, "a")[1].text
        print(title)
        print()
        monthly_1st_song.append(year)
        monthly_1st_song.append(month)
        monthly_1st_song.append(title)

        monthly_1st_songs.append(monthly_1st_song)
    except:
        print("해당 월에 들은 노래가 없습니다.")
        print()
        monthly_1st_songs.append("None")
    return monthly_1st_songs



# 선택한 월의 TOP 10 목록 가져오기
def get_monthly_top_songs(month, year, num):
    monthly_top_songs = []
    time.sleep(0.5)
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    # print(len(trs))

    for i in range(num):
        try:
            msl = []
            rank = trs[i].find_element(By.CLASS_NAME, "no").text
            tleft = trs[i].find_element(By.CLASS_NAME, "t_left")
            title = tleft.find_elements(By.TAG_NAME, "a")[1].text
            artist = trs[i].find_element(By.ID, "artistName").text
            msl.append(rank)
            msl.append(title)
            # print(title)
            if i==0:
                print(title)
                print()
            msl.append(artist)
            msl.append(year)
            msl.append(month)
            # monthly_top_songs.append(msl)
        except:
            msl = []
            print("해당 월에 들은 노래가 없습니다.")
            print()
            msl.append("None")
            # monthly_top_songs.append("None")

        monthly_top_songs.append(msl)

    # trs = tbody.find_elements(By.TAG_NAME, "tr")
    #
    # tleft1 = trs[0].find_element(By.CLASS_NAME, "t_left")
    # title1 = tleft1.find_elements(By.TAG_NAME, "a")[1].text
    # print(title1)
    #
    # for tr in trs:
    #     msl = []
    #     rank = tr.find_element(By.CLASS_NAME, "no").text
    #     tleft = tr.find_element(By.CLASS_NAME, "t_left")
    #     title = tleft.find_elements(By.TAG_NAME, "a")[1].text
    #     artist = tr.find_element(By.ID, "artistName").text
    #     msl.append(rank)
    #     msl.append(title)
    #     msl.append(artist)
    #     monthly_top_songs.append(msl)
    # print(monthly_top_songs)
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
        lists.append(get_monthly_top_songs(month, year, 5))
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
        # elif year == "2022" or year == "2021" or year == "2020" or year == "2019":
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

    # for list in my_list:
    #     print(list)
    #     print()
    #     # save_to_file(list)
    #     print(type(list))
    print(my_list)

    return True

# if year is 2015 => 크롤링 그만.
check_year()



# 월별보기 클릭 -> 1,2,3,..월 클릭 -> 각 월의 많이들은 리스트 가져오기(get_monthly_top_songs) -> 다시 월별보기 클릭 -> 반복

# lists = []
# 1월부터 12월 month[0]~month[11] 클릭
# for i in range(12):
#     month_calendar = driver.find_element(By.CLASS_NAME, "month_calendar")
#     month = month_calendar.find_elements(By.CLASS_NAME, "btn") # 12개
#     month[i].click()
#     print(str(i+1)+"월")
#     # 선택한 월의 곡 목록 가져오기
#     get_monthly_top_songs()
#     # lists.append(get_monthly_top_songs())
#     # time.sleep(2)
#     driver.find_element(By.CLASS_NAME, "d_btn_calenadar").click()
#
# time.sleep(2)


driver.quit()
