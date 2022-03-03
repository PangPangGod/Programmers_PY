#게임을 만든 동준이 2847
#https://www.acmicpc.net/problem/2847

#이게 왜 그리디임 근데

N = int(input())
storage = [int(input()) for _ in range(N)]
storage.reverse()
answer = 0

for i in range(1,N):
    if storage[i-1] <= storage[i] :
        answer += ((storage[i]-storage[i-1])+1)
        storage[i] = storage[i]-((storage[i]-storage[i-1])+1)
print(answer)