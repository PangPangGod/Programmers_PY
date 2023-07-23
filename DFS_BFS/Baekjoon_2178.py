# BaekJoon 2178 미로탐색(BFS)
from collections import deque

N,M = map(int,input().split())
grid = []

#str 형태로 받아서 list로 바꿔준다.
for i in range(N) :
    grid.append(list(map(int,list(input()))))

queue = deque([(0, 0)])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while queue :
    x,y = queue.popleft()

    for i in range(4) :
        x_x, y_y = x+dx[i], y+dy[i]

        if x_x<0 or y_y<0 or x_x>N-1 or y_y>M-1 :
            continue
        if grid[x_x][y_y] == 1 :
            grid[x_x][y_y] = grid[x][y]+1
            queue.append((x_x,y_y))

print(grid[N-1][M-1])

# for i in grid :
#     print(*i)