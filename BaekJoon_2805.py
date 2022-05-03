# 매개 변수 탐색을 진행했다.

N,M = map(int,input().split())

trees = [*map(int,input().split())]

start = 0
end = max(trees)

while start <= end :
    mid = (start+end)//2
    result = sum(map(lambda x: 0 if (x-mid)<0 else x-mid, trees))
    if result >= M :
        start = mid+1
    else :
        end = mid-1
print(end)
    