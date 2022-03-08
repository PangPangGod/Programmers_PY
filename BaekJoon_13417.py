# 카드 문자열 13417
#https://www.acmicpc.net/problem/13417
from collections import deque
answer = []
N = int(input())
for _ in range(N) :
    al_len = int(input())
    result = deque()
    standard = ''
    for k in list(input().split()) :
        if not result :
            result.append(k)
        else :
            if k > result[0] :
                result.append(k)
            else :
                result.appendleft(k)
        print(result)
    answer.append(''.join(result))
for i in answer : print(i)