#2352
#결국 노드를 구하기 = 가장 긴 증가수열 구하기 라는 것을 알아야 한다.
import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int,input().split()))

result = [nodes[0]]

def binary_search(num,lis) :
    start = 0
    end = len(lis)-1
    
    while start < end :
        mid = (start+end)//2
        if lis[mid] == num:
            start = end = mid
        if lis[mid] < num :
            start = mid+1
        elif lis[mid] > num :
            end = mid
    return start

for node in nodes :
    if result[-1] < node :
        result.append(node)
    else :
        result[binary_search(node,result)] = node

print(len(result))