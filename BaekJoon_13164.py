import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = list(map(int, input().split()))
minus = []
for i in range(1,N) :
    minus.append(nums[i]-nums[i-1])
minus.sort()
answer = 0
for i in range(N-M) :
    answer += minus[i]
print(answer)