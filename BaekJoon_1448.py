#삼각형 만들기 1148
#https://www.acmicpc.net/problem/1448
import sys
N=int(sys.stdin.readline())
leng = [int(sys.stdin.readline()) for _ in range(N)]
leng.sort()

while True :
    if len(leng)<3 :
        print(-1);break
    max_line = leng.pop()
    if max_line >= leng[-1]+leng[-2] :
        pass
    else :
        print(max_line+leng[-1]+leng[-2])
        break