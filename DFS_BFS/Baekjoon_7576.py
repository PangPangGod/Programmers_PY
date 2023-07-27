#BaekJoon 7576 토마토(2차원 BFS)
from collections import deque
import sys
input = sys.stdin.readline
M,N = map(int,input().split())

queue = deque()
grid = []

#for문 한번 돌리면서 1(토마토 퍼져나갈 곳) 체크하면서 grid에 받은 list 넣기
for i in range(N):
    temp = list(map(int,(input().split())))
    grid.append(temp)
    for k in range(M):
        if grid[i][k] == 1 :
            queue.append((i,k))


# for i in grid :
#     print(*i)

def bfs() :
    global queue
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 0
    while queue :
        curr_x, curr_y = queue.popleft()
    
        for i in range(4) :
            x_x = curr_x + dx[i]
            y_y = curr_y + dy[i]

            if 0<=x_x<N and 0<=y_y<M and grid[x_x][y_y] == 0 :
                count += 1
                grid[x_x][y_y] = grid[curr_x][curr_y]+1
                queue.append((x_x,y_y))      
bfs()

result = 0
# for i in range(N):
#     for k in range(M):
#         if grid[i][k] == 0 :
#             print(-1)
#             exit(0)
#     result = max(result,max(grid[i]))
    
# print(result-1)

# all 함수를 이용해 푸는 방법도 있다. if not all(grid[i]) -> i에 있는 값 중 하나라도 0라면
# 이 방법을 이용한다면 k번까지 도는, 즉 O(N*M)에서 O(N)으로 마지막 탐색이 짧아진다.
# 실제로도 다이나믹하진 않지만 약 90ms정도까지 짧아졌다.
for i in range(N) :
    if not all(grid[i]) :
        print(-1)
        exit(0)
    result = max(result,max(grid[i]))
print(result-1)