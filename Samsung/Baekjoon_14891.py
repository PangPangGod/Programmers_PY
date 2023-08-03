#Baekjoon 14891 톱니바퀴

# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, 
# B는 A가 회전한 방향과 반대방향으로 회전하게 된다

from collections import deque

#기준에서 왼쪽 체크(2번 인덱스, 6번 인덱스 다르면 재귀(계속 탐색), 아니면 return)
def left_check(idx,d) :
    if idx < 1 or cogs[idx][2] == cogs[idx+1][6]:
        return
    
    if cogs[idx][2] != cogs[idx+1][6] :
        left_check(idx-1,-d)

        cogs[idx].rotate(d)

def right_check(idx,d) :
    if idx > 4 or cogs[idx-1][2] == cogs[idx][6]:
        return
    
    if cogs[idx-1][2] != cogs[idx][6] :
        right_check(idx+1,-d)

        cogs[idx].rotate(d)

#main 함수
def start() :
    init_num = int(input())

    for _ in range(init_num) :
        cog_num, direction = map(int,input().split())
    
        left_check(cog_num-1,-direction)
        right_check(cog_num+1,-direction)

        cogs[cog_num].rotate(direction)


#선언
cogs = [[] for _ in range(5)]
for k in range(1,5) :
    cogs[k] = deque(list(input()))

start()

score = 0
for i in range(4) :
    score += (2**i)*int(cogs[i+1][0])

print(score)