#BaekJoon 2468
#grid 구하는 문제와 동일하게 dfs로 구현. 
#메모리 초과나서 1,101 for문을 바꿔주었더니 아슬아슬하게 통과했다.

import sys
sys.setrecursionlimit(10**6)

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

def depth_search(grid,x,y,flood) :
    if x<0 or x>=N or y<0 or y>=N :
        return False
    
    if grid[x][y] > flood and checker[x][y]:
        checker[x][y] = False
        depth_search(grid,x-1,y,flood)
        depth_search(grid,x+1,y,flood)
        depth_search(grid,x,y-1,flood)
        depth_search(grid,x,y+1,flood)
        return True
    return False

flood_area = 0
mx = 0
for target in range(max(map(max,grid))) :
    checker = [[True for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for k in range(N):
            if depth_search(grid,i,k,target) :
                flood_area += 1
    mx = max(mx,flood_area)
    flood_area = 0
    

print(mx) 
 