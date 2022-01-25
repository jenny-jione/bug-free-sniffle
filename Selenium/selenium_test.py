# 22-01-24
from selenium import webdriver
from my_info import my_path, pw

driver = webdriver.Chrome(my_path+'/Selenium/chromedriver.exe')
url = 'https://weverse.io/'
driver.get(url)

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div/button[2]').click()

# driver가 보는 대상을 팝업창(로그인창)으로 변경
driver.switch_to.window(driver.window_handles[1])

# 로그인
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[1]/input').send_keys('purples1202@gmail.com')
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/input').send_keys(pw)
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/button').click()

#  driver가 보는 대상을 메인 창으로 다시 변경
driver.switch_to.window(driver.window_handles[0])

driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div/button').click()
# 알림(종) 클릭
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div[1]/button').click()

# 알림 목록 읽기
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div[1]/div')
