#BaekJoon 10810

N, M = map(int,input().split())

arr = [0 for i in range(N)]

for _ in range(M) :
    I,J,K = map(int,input().split())

    for d in range(I-1,J) :
        arr[d] = K

print(*arr)