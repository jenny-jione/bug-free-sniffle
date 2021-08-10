# print("시작시각 입력")
# start_hour = input("시: ")
# start_minute = input("분: ")
#
# print("종료시각 입력")
# end_hour = input("시: ")
# end_minute = input("분: ")

START_HOUR = 12
START_MINUTE = 20

END_HOUR = 17
END_MINUTE = 10

start = START_HOUR * 60 + START_MINUTE
end = END_HOUR * 60 + END_MINUTE
diff = end - start
hour = int(diff / 60)
min = diff % 60

print(diff)
print(hour)
print(min)
print(f'{hour}시간 {min}분')
