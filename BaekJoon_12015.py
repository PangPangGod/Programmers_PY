#수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열을 구하는 프로그램
#이진 탐색을 이용해 리스트 내에 해당 숫자를 삽입할 수 있는 위치를 계산한 후 값을 경신한다.
#

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

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

result = [A[0]]

for i in A :
    if result[-1] < i :
        result.append(i)
    else :
        result[binary_search(i,result)] = i
    
print(len(result))
        