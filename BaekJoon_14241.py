#슬라임 합치기 14241
#https://www.acmicpc.net/problem/14241
N = int(input())
slimes = list(map(int,input().split()))
slimes.sort(reverse=True)
score = 0

while True :
    if len(slimes) == 1 :
        break
    current = slimes.pop()
    score += current*slimes[-1]
    slimes[-1]=slimes[-1]+current