#Baekjoon 7562 나이트의 이동
#나이트 움직임 기록하고 BFs로 최적의 움직임 수를 뽑아낸다.

from collections import deque
import sys

input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]

test_case = int(input())

def main() :
    N = int(input())

    grid = [[-1 for _ in range(N)] for _ in range(N)]

    start_x, start_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())

    grid[start_x][start_y] = 0
    queue = deque([(start_x,start_y)])

    while queue : 
        x, y = queue.popleft()
        
        if x == goal_x and y == goal_y:
            return grid[x][y]
        
        for i in range(8) :
            x_x, y_y = x+dx[i], y+dy[i]
            if 0<=x_x<N and 0<=y_y<N and grid[x_x][y_y] == -1:
                grid[x_x][y_y] = grid[x][y]+1
                queue.append((x_x,y_y))
    return 0

for _ in range(test_case) :
    print(main())