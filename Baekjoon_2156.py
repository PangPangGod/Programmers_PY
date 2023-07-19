#백준 2156 포도주 시식(DP)

N = int(input())
winery = []
dp = [0]*N

for _ in range(N) :
    winery.append(int(input()))

dp[0] = winery[0]
if N > 1 : 
    dp[1] = winery[0]+winery[1]
if N > 2 : 
    dp[2] = max(dp[1], winery[0]+winery[2], winery[1]+winery[2])

for k in range(3,N) :
    dp[k] = max(dp[k-1], dp[k-3]+winery[k-1]+winery[k], dp[k-2]+winery[k])

print(dp[N-1])


#dp[k-1]인 경우는 winery[k]를 마시지 않은 경우(남은 세 수중에서 최선을 구했을 때)
#나머지 두 경우는 winery[k]를 마셨을 때를 구한 경우의 수 2가지
#(k-3까지의 합과 wine[k-1]+wine[k]인 경우), (k-2까지의 합과 winery[k]의 합인 경우)