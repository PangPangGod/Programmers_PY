#14889 스타트와 링크
#그냥 백트래킹으로 구현(시간 ㅈㄴ터짐)

import sys
sys.setrecursionlimit(10**6)
people_no = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(people_no)]

visited = [ 0 for _ in range(people_no)]

result = sys.maxsize
def backtrack(x,depth) :
    global result

    if depth == people_no//2 :
        start_team = 0
        link_team = 0

        for i in range(people_no) :
            for k in range(people_no) :
                if visited[i] and visited[k] :
                    start_team += grid[i][k]
                elif not visited[i] and not visited[k] :
                    link_team += grid[i][k]
    
        result = min(result,abs(start_team-link_team))
        return

    for i in range(x,people_no) :
        if not visited[i]:
            visited[i] = 1
            backtrack(i,depth+1)
            visited[i] = 0

backtrack(0,0)
print(result)


# from itertools import combinations
# import sys

# people_no = int(sys.stdin.readline())
# grid = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(people_no)]

# #팀원별 능력치의 합 list
# member_stat = [sum(i) + sum(j) for i, j in zip(grid, zip(*grid))] #가로 세로 좌표 표현
# total_stat = sum(member_stat)//2

# result = sys.maxsize

# for combination in combinations(member_stat[:-1],people_no//2) :
#     result = min(result,abs(total_stat-sum(combination)))

# print(result)