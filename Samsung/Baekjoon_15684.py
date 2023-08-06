#15684 사다리 조작
import sys

def check() :
    for k in range(N):
        #loc 만들어서 0,k부터 출발하면서 loc[0] 하나씩 늘려감. 끝나면 k 체크.
        loc = k
        for i in range(H):
            if grid[i][loc]:
                loc += 1

            #k가 0인 경우만 아니면 왼쪽으로 갈 수 있으므로 왼쪽 체크.
            elif loc>0 and grid[i][loc-1]:
                loc -= 1
                
        if loc != k :
            return False
    return True

def depth_search(depth,x,limit) :
    if depth == limit :
        return check()
        
    for i in range(x,H) :
        for k in range(N-1) :
            if not grid[i][k]:

                grid[i][k] = 1
                # 어쨌든 if로 해도 호출하니까
                # 하나의 depth라도 true일 경우에는 전부 true가 된다.
                if depth_search(depth+1,i,limit) :
                    return True
                grid[i][k] = 0

#main
N, M, H = map(int,sys.stdin.readline().split()) 
grid = [[0 for _ in range(N)] for _ in range(H)]

for _ in range(M) :
    x, y = map(int,sys.stdin.readline().split())
    grid[x-1][y-1] = 1

answer = -1
#global 안쓰고 정답 내기
for limit in range(4) : 
    if depth_search(0,0,limit):
        answer = limit
        break
    
print(answer)

# print(check())