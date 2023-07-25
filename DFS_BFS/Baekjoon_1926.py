# Baekjoon 1926 그림
from collections import deque

def bfs(x,y,grid) : 
    queue = deque([(x,y)])
    grid[x][y] = 'v'
    count = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while queue :
        current_x, current_y = queue.popleft()
        #grid에 체킹해줌
        grid[current_x][current_y] = 'v'
        
        for i in range (4) :
            x_x = current_x+dx[i]
            y_y = current_y+dy[i]

            if N>x_x>=0 and M>y_y>=0 and grid[x_x][y_y] == 1:
                grid[x_x][y_y] = 'v'
                #갈 수 있는 그리드에 체크해줘서 중복체크 방지 및 카운트해줌
                queue.append((x_x,y_y))
                count += 1    
    return count

N,M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

counting = []

for i in range(N):
    for k in range(M) :
        if grid[i][k] == 1 :
            counting.append(bfs(i,k,grid))

print(len(counting))
#if문 해준 이유 -> counting이 0일 경우 max를 찾으면 Error
if counting :
    print(max(counting))
else :
    print(0)