# result에 첫 번째 전기줄을 넣는다.
# result의 마지막 원소와 for 문의 line이 가리키는 원소를 비교했을 때 현재원소가 크다면 result에 appned 한다.
# 작다면 이진탐색을 통해 현재 원소가 들어갈 자리를 찾는다.

N = int(input())
lines = list(map(int,input().split()))

result = [lines[0]]

def binary_search(num,lis) :
    start = 0
    end = len(lis)-1
    while start < end :
        mid = (start+end)//2
        if lis[mid] < num :
            start = mid+1
        else:
            end = mid
    return end

for line in lines: 
    if result[-1] < line :
        result.append(line)
    else :
        result[binary_search(line,result)] = line

print(len(lines)-len(result))