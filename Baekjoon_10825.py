#Baekjoon 10825 국영수

import sys

def run(N) :
    storage = {}
    for _ in range(N) :
        ip = sys.stdin.readline().rstrip().split()
        storage[ip[0]] = list(map(int, ip[1:]))

    result = sorted(storage.items(), key = lambda x : (-x[1][0],x[1][1],-x[1][2],x[0]))
    for i in result : print(i[0])

run(int(sys.stdin.readline()))
