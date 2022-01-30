### 이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(s):
    answer = []
    s = s.split(" ")
    for i in s:
        answer+=[i[k].upper() if (k+2)%2==0 else i[k].lower() for k in range(len(list(i)))]
        answer+=[' ']
    s = ''.join(answer)

    return s[:-1]