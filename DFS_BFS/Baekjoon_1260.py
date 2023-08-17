#1260 DFS와 BFS
import sys
from collections import deque

def dfs(start,visited) :
    visited[start] = False
    storage.append(start)

    for i in graph[start] :
        if visited[i] :
            dfs(i, visited)

def bfs(start,visited) :
    visited[start] = False
    queue = deque([start])
    storage.append(start)

    while queue :
        now = queue.popleft()

        for i in graph[now] :
            if visited[i] :
                visited[i] = False
                queue.append(i)
                storage.append(i)

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] 
visited = [True for _ in range(N+1)]
visited[0] = False

for _ in range(M) :
    start,end = map(int,sys.stdin.readline().split())

    graph[start].append(end)
    graph[end].append(start)

for k in graph:
    k.sort()

storage = []
dfs(V,visited[:])
print(*storage)

storage = []
bfs(V,visited[:])
print(*storage)