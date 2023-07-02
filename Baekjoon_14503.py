#백준 14503
#DFS를 통해서 4방향 점검 후 갈 수 있는곳 구하기
#이미 간 곳은 'v'로 체크해 다시 가지 않도록 했다.

import sys

#def
    
def moving(num) :
    h = [-1,0,1,0]
    v = [0,1,0,-1]
    return h[num],v[num]
    

N,M = map(int,sys.stdin.readline().split())
x,y,direction = map(int,sys.stdin.readline().split())

#0일 때 북쪽(y+1), 1일 때 동쪽(x+1), 2일 때 남쪽(y-1), 3일 때 서쪽(x-1)
coord = [list(map(int,input().split())) for i in range(N)]

count = 0

def cleaner(x,y,direction) :
    global count
    if not coord[x][y] :
        coord[x][y] = 'v'
        count += 1

    for _ in range(4) :
        mov_direction = (direction+3)%4
        mov_x,mov_y = moving(mov_direction)

        if not coord[x+mov_x][y+mov_y] :
            coord[x+mov_x][y+mov_y] = "v"
            count += 1
            cleaner(x+mov_x,y+mov_y,mov_direction)
            return
        direction = mov_direction
    
    if coord[x-mov_x][y-mov_y] == 1:
        print(count)
        return
    
    cleaner(x-mov_x,y-mov_y,mov_direction)

cleaner(x,y,direction)