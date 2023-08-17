#백준 14499 주사위 굴리기(구현)
#모든 주사위는 0의 눈금으로 시작한다는 조건을 빼먹었다.....

## def
def dice_rolls(cmd,dice_col,dice_row) :
    #북쪽, 남쪽
    if cmd == 3 :
        temp = dice_col[0]
        dice_col = dice_col[1:]
        dice_col.append(temp)
    elif cmd == 4 :
        dice_col.insert(0,dice_col.pop())

    #서쪽, 동쪽
    elif cmd == 2 :
        dice_col[1],dice_row[1] = dice_row[1],dice_col[1]
        dice_row[0],dice_col[-1] = dice_col[-1],dice_row[0]
        dice_row[0],dice_row[1] = dice_row[1],dice_row[0]
    elif cmd == 1 :
        dice_row.insert(0,dice_row.pop())
        dice_row[0],dice_col[-1] = dice_col[-1],dice_row[0]
        dice_col[1],dice_row[1] = dice_row[1],dice_col[1]
    
    return dice_col,dice_row

## input
N,M,loc_N,loc_M,K = map(int,input().split())
maps = [list(map(int,input().split())) for i in range(N)]
commands = list(map(int,input().split()))

mov_loc = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

dice_col = [0]*4
dice_row = [0]*2

## main
#지도 바깥이면 continue 찍기

for cmd in commands :
    mov_N, mov_M = mov_loc[cmd]
    mov_N = loc_N+mov_N; mov_M = loc_M+mov_M

    if mov_N < 0 or mov_N >= N or mov_M < 0 or mov_M >= M :
        continue
    
    dice_col, dice_row = dice_rolls(cmd,dice_col,dice_row)
    
    if maps[mov_N][mov_M] == 0 :
        maps[mov_N][mov_M] = dice_col[-1]
    else :
        dice_col[-1] = maps[mov_N][mov_M]
        maps[mov_N][mov_M] = 0
    
    loc_N = mov_N; loc_M = mov_M
    print(dice_col[1])



##########################################

#8월 17일날 다시 풀어본 문제 (시험대비)
# 확실히 실력이 늘었다고 생각하는게 똑같은 로직인데 코드 길이가 많이 짧아지고
# 생각도 좀 더 직관적으로 변했다.

#14499 주사위 굴리기
import sys

def dice_move(cmd,dice) :
    dice_copy = dice[:]
    if cmd == 1 :
        dice[1] = dice_copy[4]
        dice[3] = dice_copy[5]
        dice[4] = dice_copy[3]
        dice[5] = dice_copy[1]
    if cmd == 2 : 
        dice[1] = dice_copy[5]
        dice[3] = dice_copy[4]
        dice[4] = dice_copy[1]
        dice[5] = dice_copy[3]
    if cmd == 3 :
        dice[0] = dice_copy[1]
        dice[1] = dice_copy[2]
        dice[2] = dice_copy[3]
        dice[3] = dice_copy[0]
    if cmd == 4 :
        dice[0] = dice_copy[3]
        dice[1] = dice_copy[0]
        dice[2] = dice_copy[1]
        dice[3] = dice_copy[2]
        
    return dice

####### main
N, M, x, y, K = map(int, sys.stdin.readline().split())

grid = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cmds = list(map(int,sys.stdin.readline().split()))

dice= [0 for _ in range(6)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for cmd in cmds :
    if 0<=x+dx[cmd-1]<N and 0<=y+dy[cmd-1]<M :
        x,y = x+dx[cmd-1],y+dy[cmd-1]
        dice = dice_move(cmd,dice)

        if grid[x][y] == 0 :
            grid[x][y] = dice[3]
        else :
            dice[3] = grid[x][y]
            grid[x][y] = 0

        print(dice[1])