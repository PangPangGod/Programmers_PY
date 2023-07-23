# Baekjoon 5014 스타트링크

# F층 건물에 사무실 위치는 G층, 현재 위치는 S층
# 버튼은 +U OR -D밖에 못함
from collections import deque

queue = deque()

F, S, G, U, D = map(int,input().split())
visited = [0 for i in range(F+1)]

def bfs(floor) :
    queue = deque([floor])
    visited[floor] = 1
    while queue :
        current_floor = queue.popleft()

        if current_floor == G :
            return visited[current_floor]-1

        for i in (current_floor+U,current_floor-D) :
            if (i>0 and i<=F) and visited[i] == 0 :
                    queue.append(i)
                    visited[i] = visited[current_floor]+1
    return "use the stairs"

print(bfs(S))