N,M = map(int,input().split())
times = list(map(int,input().split()))

start = 1
end = max(times)*M
answer = 0

while start <= end :
    mid = (start+end)//2
    count = sum(map(lambda x:mid//x,times))
    if count<M :
        start = mid+1
    else :
        end = mid-1
print(start)