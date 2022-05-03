
#이진탐색 구현
def binary_search(list,num):
    start = 0
    end = len(list)-1
    while start<=end :
        mid = (start+end)//2
        if list[mid] == num :
            return 1
        elif num>list[mid] :
            start = mid+1
        elif num<list[mid] :
            end = mid-1
    return 0


import sys
input = sys.stdin.readline

N = int(input())
nlist = list(map(int,input().split()))
M = int(input())
mlist = list(map(int,input().split()))

nlist.sort()


for i in mlist:
    print(binary_search(nlist,i),end=' ')
    

#이외에도 딕셔너리를 만들어서 해당 값을 True로 만든 이후, 탐색하는 방법이 존재한다.
