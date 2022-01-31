# 22-01-28
# 멜론 로그인 후 마이페이지에서 각 월에 많이 들은 곡 리스트 크롤링
from selenium import webdriver
from selenium.webdriver.common.by import By
import my_info
import time

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


# 선택한 월의 곡 목록 가져오기
def get_monthly_song_list():
    monthly_song_list = []
    print("calling function")
    time.sleep(1)
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    for tr in trs:
        msl = []
        rank = tr.find_element(By.CLASS_NAME, "no").text
        tleft = tr.find_element(By.CLASS_NAME, "t_left")
        title = tleft.find_elements(By.TAG_NAME, "a")[1].text
        artist = tr.find_element(By.ID, "artistName").text
        msl.append(rank)
        msl.append(title)
        msl.append(artist)
        monthly_song_list.append(msl)
    print(monthly_song_list)
    return monthly_song_list

# 1년(12달) 클릭 후 크롤링
def get_one_year():
    lists = []
    for i in range(12):
        month_calendar = driver.find_element(By.CLASS_NAME, "month_calendar")
        month = month_calendar.find_elements(By.CLASS_NAME, "btn") # 12개
        month[i].click()
        print(str(i+1)+"월")
        # 선택한 월의 곡 목록 가져오기
        # get_monthly_song_list()
        lists.append(get_monthly_song_list())
        # time.sleep(2)
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
        else:
            print(year)

            # 1~12월 곡 리스트 가져오는 함수
            my_list.append(get_one_year())

            # 이전 년도로 이동
            driver.find_element(By.CLASS_NAME, "btn_round.small.pre").click()
            year = driver.find_element(By.CLASS_NAME, "date").text

    for list in my_list:
        print(list)

    return True

# if year is 2015 => 크롤링 그만.
check_year()



# 월별보기 클릭 -> 1,2,3,..월 클릭 -> 각 월의 많이들은 리스트 가져오기(get_monthly_song_list) -> 다시 월별보기 클릭 -> 반복

# lists = []
# 1월부터 12월 month[0]~month[11] 클릭
# for i in range(12):
#     month_calendar = driver.find_element(By.CLASS_NAME, "month_calendar")
#     month = month_calendar.find_elements(By.CLASS_NAME, "btn") # 12개
#     month[i].click()
#     print(str(i+1)+"월")
#     # 선택한 월의 곡 목록 가져오기
#     get_monthly_song_list()
#     # lists.append(get_monthly_song_list())
#     # time.sleep(2)
#     driver.find_element(By.CLASS_NAME, "d_btn_calenadar").click()
#
# time.sleep(2)


driver.quit()
