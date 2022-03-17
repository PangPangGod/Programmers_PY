#알바생 강호 1758
#https://www.acmicpc.net/problem/1758

import sys
input = sys.stdin.readline

N = int(input())
line = [int(input()) for _ in range(N)]
line.sort(reverse = True)
answer = 0
for i in range(N) :
    actual_tip = line[i]-i
    if actual_tip > 0 :
        answer += actual_tip
print(answer)