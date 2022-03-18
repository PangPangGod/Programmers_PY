#우유 축제 14720
#https://www.acmicpc.net/problem/14720
N = int(input())
stores = map(int,input().split())
answer = []

for i in stores :
    if not answer and i == 0 :
        answer.append(i)
    elif answer != [] :
        if answer[-1] == 0 and i == 1 :
            answer.append(i)
        elif answer[-1] == 1 and i == 2 :
            answer.append(i)
        elif answer[-1] == 2 and i == 0 :
            answer.append(i)