#신입사원 1946
#https://www.acmicpc.net/problem/1946
import sys
N=int(sys.stdin.readline())
for _ in range(N):
    F = int(sys.stdin.readline())
    lst = []
    for i in range(F):
        resume,interview = map(int,sys.stdin.readline().split())
        lst.append((resume,interview))
    lst.sort()
    std = lst[0][1]
    count = 1
    for k in range(1,F):
        if lst[k][1] < std :
            std = lst[k][1]
            count += 1
    print(count)