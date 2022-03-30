#풍선 맞추기 11509
#https://www.acmicpc.net/problem/11509
N=int(input())
heights = list(map(int,input().split()))
arrow_status = [0 for _ in range(1000001)]
arrow = 0

for i in range(N):
    if arrow_status[heights[i]] == 0 :
        arrow += 1
        arrow_status[heights[i]-1] += 1
    else :
        arrow_status[heights[i]] -= 1
        arrow_status[heights[i]-1] += 1
print(arrow)