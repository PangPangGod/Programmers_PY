import sys
input = sys.stdin.readline

N = int(input())
regions = list(map(int,input().split()))
limit = int(input())

regions.sort()

start = 1
end = regions[-1]

answer = 0

while start <= end :
    mid = (start+end)//2
    temp = sum(map(lambda x:mid if x>=mid else x, regions))
    if temp<=limit :
        start = mid+1
        answer = mid
    else :
        end = mid-1

print(answer)