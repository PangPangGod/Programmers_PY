#15903 카드 합체 놀이
import heapq

N,M = map(int,input().split())
que = []

for i in map(int,input().split()) :
    heapq.heappush(que,i)

while M :
    heapq.heappush(que,(result := heapq.heappop(que)+heapq.heappop(que)))
    heapq.heappush(que,result)
    M -= 1

print(sum(que))