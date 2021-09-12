# 쿠키 목록 불러와서 필요없는 부분 자른 후에 새 파일에 저장하는 프로그램
# 21-09-12

from my_info import my_path

f = open(my_path+"/Toy/crk_cookies.txt", 'r', encoding='UTF8')
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
lines = f.readlines()

cookies = []
for line in lines:
    # replace를 하고 다시 line에 대입해주어야 값이 업데이트된다.
    line = line.replace("☆","")
    line = line.replace("★","")
    cookies.append(line.split('[')[0])

print(cookies)
print(len(cookies))

file = open(my_path+"/Toy/cookies.txt", 'w', encoding='UTF8')
for cookie in cookies:
    file.write(cookie)
    file.write("\n")
