#백준 1158 요세푸스 문제

from collections import deque
N, K = map(int, input().split())
JP = deque([i for i in range(1,N+1)])

result = []
while JP :
    JP.rotate(len(JP)-K)
    result.append(JP.pop())

print("<",end="")
print(*result,sep=", ",end="")
print(">",end="")