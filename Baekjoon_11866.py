# Baekjoon 11866

## deque 이용해서 killer 전까지는 popleft로 빼서 뒤에 더해주고
## killer에 해당하는 인덱스만 pop 해주면 쉽게 풀 수 있다.
from collections import deque

N, killer = map(int,input().split())


victim = deque([i+1 for i in range(N)])
result = []

while victim :
    for i in range(killer-1) :
        victim.append(victim.popleft())
    result.append(victim.popleft())

print("<",end="")
print(*result,sep=', ',end="")
print(">",end="")