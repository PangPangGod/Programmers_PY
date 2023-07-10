# 색종이의 가로, 세로 길이는 10
# 입력되는 좌표는 색종이의 (x,y) 왼쪽 밑 값
# 따라서 높이 좌표는 x+10, 너비 좌표는 y+10
# 겹친다면 겹치는 부분*2 만큼 빼주면 된다.

# 사각형 좌표는 a,b가 입력값이라고 할 때
# (a,b) (a,b+10) (a+10,b+10), (a+10,b)가 된다.

# 먼저 사각형 좌표를 구해보자

#BaekJoon 2563

N = int(input())

paper = [[0 for i in range(100)] for _ in range(100)]


for i in range (N):
    X,Y = map(int,input().split())

    for i in range(X,X+10) :
        for j in range(Y,Y+10):
            paper[i][j] = 1

result = 0

for k in paper :
    result += sum(k)

print(result)