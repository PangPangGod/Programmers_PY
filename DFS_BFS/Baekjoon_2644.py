# Baekjoon 2644 촌수계산
# 앞으로 방문체크 할 때, 특히 단계별로 셀 때 체크 한 다음 숫자를 넣는 방식을 쓰자
# ex) visited[relation] = visited[curr_people]+1
from collections import deque
import sys

input = sys.stdin.readline

def draw_list(start,end,storage) :
    """ 인접 리스트 그리기 """
    storage[start].append(end)
    storage[end].append(start)
    return storage

def bfs(goal_x) :
    global goal_y, storage, visited
    queue = deque([goal_x])
    visited[goal_x] = 0

    #방문해서 맞으면 현재까지 더해온 촌수 return
    while queue :
        curr_people = queue.popleft()
        if curr_people == goal_y :
            return visited[goal_y]
        #아니면 방문체크해서 방문시키고 queue에 추가
        for relation in storage[curr_people] :
            if visited[relation] == 0 :
                queue.append(relation)
                visited[relation] = visited[curr_people]+1
    return -1
              
#main
people = int(input())
goal_x,goal_y = map(int,input().split())
num_of_relation = int(input())

#관계저장, 방문체크 설정하기.
storage = [[] for _ in range(people+1)]
visited = [0 for _ in range(people+1)]

#인접리스트 그려서 저장하기.
for _ in range(num_of_relation):
    x,y = map(int,input().split())
    storage = draw_list(x,y,storage)
     
print(bfs(goal_x))