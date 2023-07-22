#Baekjoon 21608 상어 초등학교

# 조건
# 1. 비어 있는 칸 중에서 <좋아하는 학생>이 가장 많은 칸
# 2. 1번이 여러 개 일 때, 인접한 칸 중에서 <비어있는 칸>이 가장 많은 칸
# 3. 2번이 여러 개 일 때, 행의 번호가 가장 작은 칸으로
# 4. 3번이 여러 개 일 때, 열의 번호가 가장 작은 칸으로

#조건 다 적어주고 참조하면서 하면 될듯??

## arr
N = int(input())

#사각형 생성
grid = [[0 for _ in range(N)] for _ in range(N)]

#dictionary로 학생 번호와 선호하는 학생 받기.
prefer = {}

dx = [1,0,-1,0]
dy = [0,1,0,-1]

#사방 체크하는 함수(조건에 맞는지, 비어 있는지?)
def checker(x,y,grid,studentNo) :
    global prefer, love_score, empty_score
    #기존 좌표에서 벗어났을 경우
    if x < 0 or y < 0 or x >= N or y >= N:
        return 
    if studentNo in prefer and grid[x][y] in prefer[studentNo] :
        love_score += 1
    if grid[x][y] == 0 :
        empty_score += 1
    return

## 일단 자리배치부터 시작하자.
for _ in range(N**2) :
    student_info_temp = list(map(int, input().split()))
    #딕셔너리로 학생 번호와 좋아하는 학생 저장하기.
    studentNo = student_info_temp[0]
    
    prefer[studentNo] = tuple(student_info_temp[1:])
    
    storage = []

    love_score = 0 #좋아하는 학생 세기
    empty_score = 0 #비어있는 자리 세기

    for i in range(N) :
        for k in range(N) :
            #점수는 여기서 초기화
            love_score = 0
            empty_score = 0

            #비었으면 인접조사 ㄱㄱ (love_score, empty_score 뽑아서 넣기)
            if grid[i][k] == 0 :
                checker(i+1, k, grid, studentNo)
                checker(i, k+1, grid, studentNo)
                checker(i-1, k, grid, studentNo)
                checker(i, k-1, grid, studentNo)

                storage.append(tuple([love_score,empty_score,i,k]))

    #storage 받아서 key별로 정렬, -x[0] : 내림차순
    storage = sorted(storage, key=lambda x:(-x[0],-x[1],x[2],x[3]))
    
    grid[storage[0][2]][storage[0][3]] = studentNo

    # 다음 수 넣어야 하므로 storage 초기화
    storage = []

# #잘됨굿
# print('==============')
# for i in grid :
#     print(*i)

answer = 0
for i in range(N) :
    for k in range(N) :
        counter = 0
        for id in range(4) :
            x_x = i+dx[id]
            y_y = k+dy[id]
            if (x_x<N and y_y<N and x_x>=0 and y_y>=0):
                if grid[x_x][y_y] in prefer[grid[i][k]] :
                    counter += 1
        if counter == 0 :
            continue
        else :
            answer += 10**(counter-1)

print(answer)