#15685 드래곤 커브
# x,y 통상과는 반대로 주어져있다.
dx = [0,-1,0,1]
dy = [1,0,-1,0]

grid = [[0 for _ in range(101)] for _ in range(101)]
dragon_curve = [list(map(int,input().split())) for _ in range(int(input()))]

# for i in dragon_curve :
#     print(*i)

result = []

while dragon_curve :
    y, x, direction, goal = dragon_curve.pop()
    grid[x][y] = 1

    curves = [direction]

    #drawing curve
    #맨 뒤(최근)에서부터 뽑아서 움직임 추가해야 함
    for i in range(goal) :
        for k in range(len(curves)-1,-1,-1):
            curves.append((curves[k] + 1) % 4)

    #커브 추가 이후에 커브 따라 움직여주면서 조건 벗어나지 않으면 체크해줌.
    for curve in curves :
        x,y = x+dx[curve], y+dy[curve]

        if x<0 or x>100 or y<0 or y>100 :
            break
        else :
            grid[x][y] = 1

#사각형인지 체크하는 함수.
def check_square(grid, i, k) :
   if  grid[i][k] and grid[i+1][k] and grid[i][k+1] and grid[i+1][k+1] :
       return True
   return False

result = 0

#사각형이면 더함.
for i in range(100) :
    for k in range(100) :
        if check_square(grid,i,k) :
            result += 1

print(result)
