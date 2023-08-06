# 트리의 부모 찾기(BFS) 11725
from collections import deque

n_node = int(input())
network = [[] for _ in range(n_node+1)]
parent = [0 for _ in range(n_node+1)]
visited = [0 for _ in range(n_node+1)]

for i in range(1,n_node) :
    start,end = map(int,input().split())
    
    network[start].append(end)
    network[end].append(start)

queue = deque([1])
visited[1] = 1
while queue :
    current_node = queue.popleft()

    for i in network[current_node] :
        
        if parent[i] == 0 and visited[i] == 0:
            parent[i] = current_node
            visited[i] = 1
            queue.append(i)
        

for i in range(2,n_node+1) :
    print(parent[i])