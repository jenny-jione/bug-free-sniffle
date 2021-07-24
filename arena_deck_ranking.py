with open('arena.txt', 'r', encoding='UTF8') as f:
    text = f.read()

tmp = text.split() # 공백을 기준으로 text를 나누어서 리스트로 만든다.


deck_list = []

for x in tmp:
    if len(x) == 5:
        deck_list.append(x)

deck_list_letter_sorted= []

# 리스트 한 요소 안에서 글자 순서를 정렬하기
for deck in deck_list:
    temp = list(deck)
    temp.sort()
    str=''.join(temp)
    deck_list_letter_sorted.append(str)
###


deck_list_letter_sorted.sort()


deck_ranking = []

deck_list_no_duplicate = set(deck_list_letter_sorted)

for deck in deck_list_no_duplicate:
    deck_ranking.append((deck_list_letter_sorted.count(deck), deck))

deck_ranking.sort(reverse=True)

for result in deck_ranking:
    print(result[1], ":", result[0])

