#수 묶기 1744
#https://www.acmicpc.net/problem/1744
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
pos = []
neg = []
answer = 0
for _ in range(N) :
    temp = int(input())
    if temp > 1 :
        pos.append(temp)
    elif temp == 1 :
        answer += 1
    else :
        neg.append(temp)
        
pos.sort(reverse=True);pos=deque(pos)
neg.sort();neg=deque(neg)

while pos :
    temp1 = pos.popleft()
    if len(pos) == 0 :
        answer += temp1
        break
    else :
        answer += temp1*pos[0]
        pos.popleft()
while neg :
    temp2 = neg.popleft()
    if len(neg) == 0 :
        answer += temp2
        break
    else :
        answer += temp2*neg[0]
        neg.popleft()
        
print(answer)
        


