import heapq
N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap,int(input()))

answer = 0
while True :
    if len(heap) == 1:
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += a+b
    heapq.heappush(heap,a+b)

print(answer)