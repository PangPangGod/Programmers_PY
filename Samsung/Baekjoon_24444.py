#24444 알고리즘 수업 1 - 너비 우선 탐색 1
from collections import deque
import sys

input = sys.stdin.readline
nodes, networks, start_node = map(int,input().split())
node_graph = dict()

for _ in range(networks) :
    start, end = map(int,input().split())

    if node_graph.get(start,False) :
        node_graph[start].append(end)
    else :
        node_graph[start] = [end]
    
    if node_graph.get(end,False) :
        node_graph[end].append(start)
    else :
        node_graph[end] = [start]

for i,k in node_graph.items() :
    node_graph[i] = sorted(k)

#####################################################

visited = [0 for _ in range(nodes+1)]
visited[start_node] = 1
queue = deque([start_node])

rank = 2
while queue :
    current_pop = queue.popleft()

    for i in node_graph[current_pop] :
        if visited[i] == 0 :
            queue.append(i)
            visited[i] = rank
            rank += 1

for i in range(1,nodes+1) :
    print(visited[i])
