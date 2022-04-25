#블루레이 녹화
import sys
input= sys.stdin.readline

N,M = map(int,input().split())
bluerays = [*map(int,input().split())]

start = max(bluerays)
end = sum(bluerays)


while start <= end :
    mid = (start+end)//2
    tmp = 0
    tmp2 = 0
    
    for num in bluerays :
        if tmp+num > mid :
            tmp2 += 1
            tmp = 0
        tmp += num
    tmp2 += 1 if tmp else 0
        
    if tmp2 <= M :
        end = mid-1
    else :
        start = mid+1
        
print(start)