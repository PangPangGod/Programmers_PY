#16235 나무 재테크

#가장 처음에 양분은 모든 칸에 5만큼 들어있다.

#봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
#하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
#만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

#여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
#각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
#소수점 아래는 버린다.

#가을에는 나무가 번식한다. 
#번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
#어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 
#상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

#겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
#각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

#K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

land = [[5 for _ in range(N)] for _ in range(N)]
S2D2 = [list(map(int,input().split())) for _ in range(N)]

alive_tree = [[ [] for _ in range(N)] for _ in range(N)] 

#append input
for _ in range(M) :
    x, y, age = map(int,input().split())
    alive_tree[x-1][y-1].append(age)

#가을에 나무 번식할 때 대각선
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K) :
    #봄 + 여름
    # 조건 만족 안하면 바로 더해줘버리면 된다.

    #정렬하고 시작하는 이유 : 가을에 나무 추가해서 봄에 양분 줄때 자르므로.

    for i in range(N) :
        for k in range(N) : 
            if alive_tree[i][k] :
                alive_tree[i][k].sort()

                for tree_ages in range(len(alive_tree[i][k])):
                    if land[i][k] >= alive_tree[i][k][tree_ages] :
                        land[i][k] -= alive_tree[i][k][tree_ages]
                        alive_tree[i][k][tree_ages] += 1
                    else :
                        for tree_to_pop in range(tree_ages,len(alive_tree[i][k])):
                            popped = alive_tree[i][k].pop()
                            land[i][k] += popped//2
                        break

    #가을
    #번식하는 나무는 나이가 5의 배수, 즉 i%5 == 0일 때.
    # 8번 돌면서 체크함.

    for x in range(N) :
        for y in range(N) :
            for ages in range(len(alive_tree[x][y])) :
                if alive_tree[x][y][ages] % 5 == 0 :
                    for d in range(8) : 
                        x_x, y_y = x+dx[d], y+dy[d]

                        if 0<=x_x<N and 0<=y_y<N :
                            alive_tree[x_x][y_y].append(1)

    #겨울
    #S2D2가 땅에 양분을 추가함.
    for i in range(N) :
        for k in range(N) :
            land[i][k] += S2D2[i][k]

#result
count = 0
for i in range(N) :
    for k in range(N) :
        if alive_tree[i][k] :
            count += len(alive_tree[i][k])

print(count)