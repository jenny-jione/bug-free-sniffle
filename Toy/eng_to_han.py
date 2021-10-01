# 한영변환 안돼서 영어로 써진 문자열을 한글로 바꿔주는 함수
# 초성 중성 종성 구분해서 글자 모양대로 배열
# 21-09-30

# 한영변환 안돼서 영어로 써진 문자열을 한글로 바꿔주는 프로그램
dict = {'a':'ㅁ','b':'ㅠ','c':'ㅊ','d':'ㅇ','e':'ㄷ','E':'ㄸ','f':'ㄹ','g':'ㅎ','h':'ㅗ','i':'ㅑ','j':'ㅓ','k':'ㅏ','l':'ㅣ','m':'ㅡ','n':'ㅜ','o':'ㅐ','O':'ㅒ','p':'ㅔ','P':'ㅖ','q':'ㅂ','Q':'ㅃ','r':'ㄱ','R':'ㄲ','s':'ㄴ','t':'ㅅ','T':'ㅆ','u':'ㅕ','v':'ㅍ','w':'ㅈ','W':'ㅉ','x':'ㅌ','y':'ㅛ','z':'ㅋ'}
jamo = {'ㄱ':1,'ㄴ':1,'ㄷ':1,'ㄹ':1,'ㅁ':1,'ㅂ':1,'ㅅ':1,'ㅇ':1,'ㅈ':1,'ㅊ':1,'ㅋ':1,'ㅌ':1,'ㅍ':1,'ㅎ':1,'ㅏ':2,'ㅑ':2,'ㅓ':2,'ㅕ':2,'ㅗ':2,'ㅛ':2,'ㅜ':2,'ㅠ':2,'ㅡ':2,'ㅣ':2,'ㅐ':2,'ㅔ':2,'ㅒ':2,'ㅖ':2}


def to_hangeul(word):
    h_str = ""
    for x in word:
        h_str+=dict[x]

    print(h_str)

    length = len(h_str)
    result = []

    for i in range(length):
        # 현재 letter가 모음일 때
        if jamo[h_str[i]]==2:
            # 현재 letter과 바로 앞 letter을 리스트에 추가한다. (자음-모음)
            # 모음 앞에 있는 letter는 무조건 자음이고, 무조건 현재 모음이 속한 글자의 초성이기 때문
            result.append(h_str[i-1:i+1])

            # 현재 letter의 앞앞 letter(i-2)가 자음일 때 (자음-자음-모음 일 때)
            if i>3 and jamo[h_str[i-2]]==1:
                # i-2는 앞 글자의 종성이기 때문에 현재 글자 말고 이전 글자를 변경.
                # 초성,중성,종성이 모두 있으니 i-4:i-1
                result[-2] = h_str[i-4:i-1]

        # 맨 마지막 letter가 자음일 경우, 마지막 글자의 종성이므로
        if i==length-1 and jamo[h_str[i]]==1:
            # 마지막 글자 변경. i-2,i-1,i
            result[-1] = h_str[i-2:]

    return result

def syllable(han):
    # 각 자모와 초성/중성/종성 정보값을 저장하는 리스트
    result = []
    for x in han:
        temp = []
        onset = []
        nucleus = []
        coda = []

        onset.append(x[0])
        nucleus.append(x[1])

        if len(x)==3:
            coda.append(x[2])

        temp.extend(onset+nucleus+coda)
        result.append(temp)

    return result

word = "dkssudgktpdy"
han = to_hangeul(word)
print(han)

info = syllable(han)
print(len(info))
print(info)
