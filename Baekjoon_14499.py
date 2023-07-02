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