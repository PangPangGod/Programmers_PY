#2+1 세일 11508
import sys
input = sys.stdin.readline
N = int(input())
temp = [int(input()) for _ in range(N)]
temp.sort(reverse=True)
temp = [temp[i:i+3] for i in range(0, len(temp),3)]

answer = 0
for i in temp :
    if len(i) != 3 :
        answer += sum(i)
    else :
        answer += i[0]+i[1]

print(answer)