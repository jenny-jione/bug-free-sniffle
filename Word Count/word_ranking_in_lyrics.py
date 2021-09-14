# 단어 출현 순위
# 21-08-10

with open('C:/Users/장지원/Desktop/dev/Word Count/spring_day.txt', 'r', encoding='UTF8') as f:
    text = f.read()

word_list = text.split()
# word_list.remove('\n')
# word_list.remove(' ')

word_list_no_duplicate = list(set(word_list))

word_count = []

print(len(word_list_no_duplicate))

for word in word_list_no_duplicate:
    word_count.append((word_list.count(word), word))

n=1
for result in sorted(word_count, reverse=True):
    if n>10:
        break
    else:
        print(result[0], ':', result[1])
        n=n+1


"""
의문점
1. split() 함수는 자동으로 공백을 기준으로 자르는 거 맞나?
2. 그러면 \n은?? 얘도 따로 remove 안해도 되는 건가?
왜냐면 remove('\n') 했더니 그런 원소는 없다고 에러가 뜸
3. append()는 인자가 1개라고 알고 있는데 왜 저기에 두개가 들어가는거지..
"""
