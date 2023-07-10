#Baekjoon_18111

import sys
#기본적으로 0부터 256까지 전부 돌려서 확인하고 최솟값을 출력하는 방식을 사용했다.

def getter(Y,X,INV,grid,target,upper,downner,min_time,min_floor) :
    for i in range(Y) :
        for k in range(X) :
            if grid[i][k] >= target :
                downner += grid[i][k]-target
            elif grid[i][k] < target :
                upper += target-grid[i][k] 

    #인벤토리에 있는 값과 땅 파서 얻은 흙의 값의 합이 올리기에 드는 흙의 합보다 적으면 진행할 수 없기 때문.
    if downner + INV >= upper :
        #시간 계산하기
        if min_time >= (downner*2)+upper :
            min_time = (downner*2)+upper
            min_floor = target
    return min_time, min_floor
    
min_time = sys.maxsize
min_floor = 1
Y, X, INV = map(int, input().split())
grid = []

for _ in range(Y) :
    grid.append(list(map(int,input().split())))

for target in range(257) :
    upper, downner = 0, 0
    min_time, min_floor = getter(Y,X,INV,grid,target,upper,downner,min_time,min_floor)

print(min_time,min_floor)