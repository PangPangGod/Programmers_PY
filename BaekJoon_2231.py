#분해합 2231
#https://www.acmicpc.net/problem/2231
N = int(input())
answer = 0
for i in range(1,N):
    sum_i = i+sum(list(map(int,list(str(i)))))
    if sum_i == N :
        answer = i
        break
if answer != 0 :
    print(answer)
else :
    print(0)
