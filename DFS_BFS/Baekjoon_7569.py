#Baekjoon 7569 토마토

#상자의 크기를 나타내는 M,N과
#쌓아올린 상자, Height를 나타내는 H
#N이 세로, M이 가로
from collections import deque
import sys
input = sys.stdin.readline

M,N,H = map(int,input().split())
queue = deque()

grid = [[list(map(int,input().split())) for _ in range(N)] for k in range(H)]

#1인 경우 찾아서 우선적으로 넣어줘야 시간 초과 넘겨줄 수 있다.
for i in range(H) :
    for k in range(N) :
        for m in range(M) :
            if grid[i][k][m] == 1 :
                queue.append((i,k,m))

dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while queue :
    z,x,y = queue.popleft()

    #z축, x축, y축을 포함한 6방향으로 돌려줘야 한다.
    for i in range(6) :
        z_z, x_x, y_y = z+dz[i], x+dx[i], y+dy[i]

        if z_z<0 or x_x<0 or y_y<0 or z_z>=H or x_x>=N or y_y>=M :
            continue

        if grid[z_z][x_x][y_y] == 0 :
            queue.append((z_z,x_x,y_y))
            grid[z_z][x_x][y_y] = grid[z][x][y]+1

# for i in grid : 
#     for j in i :
#         print(*j)
#     print('=======')

answer = 0

for gri in grid :
    for k in gri :
        for n in k :
            if n == 0 :
                print(-1)
                exit(0) #exit(0) 성공한 순간 프로그램 실행이 끝나게 된다.
                        #따라서 -1 출력하고 종료한다.
        answer = max(answer, max(k))
print(answer-1)