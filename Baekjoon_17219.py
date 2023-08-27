import sys

N, M = map(int,sys.stdin.readline().split())

storage = {}

for _ in range(N) : 
    address, password = sys.stdin.readline().rstrip().split()
    storage[address] = password

for _ in range(M) :
    key = sys.stdin.readline().rstrip()
    print(storage[key])

