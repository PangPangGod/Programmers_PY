#16234 인구 이동

#BFS 사용해서 조건 맞으면 GRID 체크해서 값을 바꿔주면 되는 구현 문제
#너무 길게 쓰지 말고 nest 3중 이상 되는것 같으면 함수 선언하자.

from collections import deque

def bfs(x,y) :
    global border, dx, dy, L, R
    res = []

    queue = deque()
    queue.append((x,y))
    res.append((x,y))
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for i in range(4) :
            x_x = curr_x+dx[i]
            y_y = curr_y+dy[i]

            if 0<= x_x <N and 0<= y_y <N and visited[x_x][y_y] == 0 :
                if L <= abs(border[x_x][y_y]-border[curr_x][curr_y]) <= R :

                    visited[x_x][y_y] = 1
                    
                    queue.append((x_x,y_y))
                    res.append((x_x,y_y))
    return res

#main
N,L,R = map(int,input().split())
border = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

check = 0
day = 0

while True :
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for k in range(N):
            if visited[i][k] == 0 :
                visited[i][k] = 1
                storage = bfs(i,k)
                
                if len(storage) > 1 :
                    check = True
                    storage_num_to_go = sum(border[n][m] for n,m in storage)//len(storage)
                    
                    for x, y in storage :
                        border[x][y] = storage_num_to_go

    if check == False :
        print(day)
        break

    check = False
    day += 1
    