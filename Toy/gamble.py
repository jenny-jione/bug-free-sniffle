# 주사위 던지기: 원하는 숫자가 나올 때까지 던져야 하는 횟수를 계산하는 프로그램
# 21-09-15

import random
import collections
import numpy as np
import matplotlib.pyplot as plt

gamble = [1, 2, 3, 4, 5, 6]

# 1이 나올 때까지의 시행횟수 구하기
def count_implement():
    count = 0
    while True:
        count = count + 1
        pick = random.choice(gamble)
        # print(pick)
        if pick == 1:
            break
    return count

result = []
for i in range(1000):
    cnt = count_implement()
    result.append(cnt)

# print(result)

avg = sum(result)/len(result)
med = np.median(result)

print("average:", avg)
print("median:", med)
max_value = max(result)
print("max:",max_value)

# collections 모듈로 리스트 요소의 빈도수 세기
dict = collections.Counter(result)
# key: n번 만에 나옴, values: n번의 빈도
# ex) 1000번 중에 첫번째만에 나온 경우가 100번이라면, key:1, value:100

# 딕셔너리 정렬
sdict = sorted(dict.items())
# print(sdict)

implement = []
cnt = []
for x in sdict:
    implement.append(x[0])
    cnt.append(x[1])
    print(implement[-1],":",cnt[-1])

# 막대그래프 그리기
x = np.arange(len(dict))


plt.bar(x,cnt)
plt.xticks(x,implement)

plt.show()
