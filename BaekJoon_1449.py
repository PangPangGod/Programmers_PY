# 수리공 항승 1449
# https://www.acmicpc.net/problem/1449

N,tape = map(int,input().split())
holes = list(map(int,input().split()))
holes.sort()
answer = 1
current_tape = tape
for i in range(1,N):
    temp = holes[i]-holes[i-1]
    if current_tape-temp > 0 :
        current_tape -= temp
    else :
        answer += 1
        current_tape = tape

print(answer)