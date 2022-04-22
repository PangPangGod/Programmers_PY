#mid에 따라 해당 라우터를 몇개까지 설치할 수 있는지를 알아보고
#충분한 설치 거리를 찾지 못했다면 거리를 줄여주고
#설치된 집이 더 많다면 거리를 늘려준다.

import sys
input = sys.stdin.readline

N,C = map(int,input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1]-houses[0]
result = 0
while start<=end :
    mid = (start+end)//2
    count = 1
    current = houses[0]
    
    for i in range(1,N):
        if houses[i] >= current+mid :
            count += 1
            current = houses[i]
            
    if count >= C :
        result = mid
        start = mid+1
    elif count < C :
        end = mid-1
        
print(result)