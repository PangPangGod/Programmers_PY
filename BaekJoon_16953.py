# A → B 16953
# https://www.acmicpc.net/problem/16953
# 제한조건을 복잡하게 걸었다가 실패했음 (v[0] > 10**9)
# bfs 알고리즘에 따라 계산한 결과를 출력하는 간단한 문제.
from collections import deque
a,b = map(int,input().split())
def dfs(start,target):
    queue = deque()
    queue.append([start,1])
    while queue :
        v = queue.popleft()
        if v[0] == target:
            return v[1]
        
        if v[0]*2 <= target :
            queue.append([v[0]*2,v[1]+1])
        if int(str(v[0])+'1') <= target :
            queue.append([int(str(v[0])+'1'),v[1]+1])
    return -1

print(dfs(a,b))