#이분탐색을 이용해 해결하였다.
#각각의 정보를 받아서 1부터 end(가장 크게 나눌 수 있는 값)
#sum 해주고 이를 mid값으로 나누어 나눌 수 있는 선의 개수를 구하였다.
#만약에 선의 개수가 크다면 더 큰 값으로 나누어야 하므로 start로, 이외에는 반대의 경우로 연산하였다.

N,K = map(int,input().split())

lines = []
for i in range(N):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end: 
    mid = (start + end)//2
    sums = 0
    for k in lines :
        sums += k//mid
    if sums >= K :
        start = mid+1
    else :
        end = mid-1
print(end)
