#Baekjoon 1764 듣보잡
#윾시 딕셔너리다. 이번에도 input 받고 돌리는데 for문 2번 썼는데 안 쓰는 방법이 없을까?

from collections import defaultdict
import sys

havnt_heard, havnt_seen = map(int, sys.stdin.readline().split())

people_dict = defaultdict(lambda :0)

for _ in range(havnt_heard) :
    n = sys.stdin.readline()
    people_dict[n] = n

cnt = 0
lst = []

for _ in range(havnt_seen) :
    m = sys.stdin.readline()
    if people_dict.get(m) :
        cnt += 1
        lst.append(m)

lst.sort()
print(len(lst))
print(*lst,sep='')