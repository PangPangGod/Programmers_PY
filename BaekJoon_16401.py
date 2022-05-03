#과자의 길이가 구간의 중간값일 때, 과자를 나누어 줄 수 있는지 확인한다.
#모든 과자의 길이를 중간값으로 나눈 합이 나누어야 하는 인원 수보다 많거나 같은 경우 중 최댓값을 구해준다.
import sys
input = sys.stdin.readline

M,N = map(int,input().split())
snacks = list(map(int,input().split()))

start = 0
end = max(snacks)
answer = 0

while start <= end :
    tmp = 0
    mid = (start+end)//2
    if mid == 0 :
        tmp = 0
        break
    
    for i in snacks :
        if i >= mid :
            tmp += (i//mid)

    if tmp>=M :
        start = mid+1
        answer = mid
    else :
        end = mid-1

print(answer)