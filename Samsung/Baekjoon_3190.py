# Baekjoon 3190 뱀

#뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킨다
#만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다 (즉, 몸 길이가 증가한다.)
#만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸 길이는 변하지 않는다.

from collections import deque

### def
def turn_snake(cmd,idx) :
    if cmd == "L" : return (idx-1)%4
    else : return (idx+1)%4

### init
#grid check
N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]

#place apple at map
for _ in range(int(input())) : 
    x, y = map(int,input().split())
    grid[x-1][y-1] = 1 #사과 있다는 뜻

#moving cmd in deque
moving_cmd = []

for _ in range(int(input())):
    x, y = input().split()
    moving_cmd.append((int(x),y))

# for i in grid :
#     print(*i)

moving= [(0,1),(1,0),(0,-1),(-1,0)]
moving_idx = 0 # 처음 움직임은 0(동쪽으로)

time = 0
time_idx = 0
snake = deque([(0,0)])
x_loc, y_loc = 0, 0 # 좌표

### main

# 시간 체크할때 빼서 생각하니까 자꾸 오류나서 time 하나씩 더해주면서 moving_cmd에 있는 시간까지 가게 만들었다.
# 도착한 이후에는 index를 옮겨 다음 방향으로 돌리고 해당 방향으로 계속 전진시킴.

while True :
    time += 1
    x_loc += moving[moving_idx][0]
    y_loc += moving[moving_idx][1]

    if 0>x_loc or x_loc>=N or 0>y_loc or y_loc>=N or (x_loc,y_loc) in snake :
        break
    
    if grid[x_loc][y_loc] == 1 :
        grid[x_loc][y_loc] = 0
        snake.append((x_loc,y_loc))
    else :
        snake.append((x_loc,y_loc))
        snake.popleft()

    if time == moving_cmd[time_idx][0] :
        moving_idx = turn_snake(moving_cmd[time_idx][1],moving_idx)

        if time_idx+1 < len(moving_cmd) :
            time_idx+=1

print(time)