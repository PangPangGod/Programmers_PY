#Baekjoon 2606 바이러스(BFS)
from collections import deque

# 갈 수 있는 경로를 담은 인접리스트 그리기
def draw_list(start,end,storage) :
    storage[start].append(end)
    storage[end].append(start)
    return storage

pc_num = int(input())
network_num = int(input())
storage = [[] for _ in range(pc_num+1)]

#network 정보 받아서 인접리스트 함수에 넣어주기 -> 인접 리스트 완성
for _ in range(network_num) :
    start, end = map(int,input().split())
    storage = draw_list(start,end,storage)

#BFS
queue = deque([1])
visitied = [ False for _ in range(pc_num+1)]

count = 0
while queue :
    current_pc = queue.popleft()
    # 맨 처음 1도 True처리 해줘야 함.
    visitied[current_pc] = True

    for pc in storage[current_pc] :
        if not visitied[pc]:
            visitied[pc] = True
            queue.append(pc)
            count += 1

print(count)