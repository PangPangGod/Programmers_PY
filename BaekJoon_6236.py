N,M = map(int,input().split())
budget = []

for _ in range(N):
    budget.append(int(input()))

start = min(budget)
end = sum(budget)
answer = 0

while start <= end :
    mid = (start+end)//2
    count = 0
    mid_temp = 0
    for i in budget :
        if mid_temp < i :
            count += 1
            mid_temp = mid
        mid_temp -= i
    if count > M or mid < max(budget):
        start = mid+1
    else  :
        end = mid-1
        answer = mid
        
print(answer)
        