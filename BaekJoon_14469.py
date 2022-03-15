#소가 길을 건너간 이유 14469
#https://www.acmicpc.net/problem/14469
N = int(input())
farm = [list(map(int,input().split())) for _ in range(N)]
farm.sort()
time = 0
for cow in farm :
    if time < cow[0] :
        time = cow[0]
        time += cow[1]
    else :
        time += cow[1]
print(time)