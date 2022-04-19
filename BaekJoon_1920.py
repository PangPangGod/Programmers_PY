import sys
input = sys.stdin.readline

N = int(input())
list_a=[]
list_a = list(map(int,input().split()))

M = int(input())
list_b=[]
list_b = list(map(int,input().split()))
    
#이분탐색을 위해 오름차순 정렬
list_a.sort()

def binary_search(list,target):
    start = 0
    end = len(list)-1
    
    while start<=end :
        mid = (start+end)//2
        if target == list[mid] :
            return 1
        elif target > list[mid] :
            start = mid+1
        elif target < list[mid] :
            end = mid-1
    return 0

for i in list_b :
    print(binary_search(list_a,i))
            
    