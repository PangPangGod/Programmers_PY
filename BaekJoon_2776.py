#암기왕
import sys
input= sys.stdin.readline

def binary_search(num,target):
    start = 0
    end = len(target)-1
    while start <= end :
        mid = (start+end)//2
        if num == target[mid] :
            return 1
        elif num>target[mid] :
            start = mid+1
        elif num<target[mid] :
            end = mid-1
    return 0


T = int(input())
for _ in range(T):
    N = int(input())
    first_note = list(map(int, input().split()))
    first_note.sort()
    M = int(input())
    second_note = list(map(int, input().split()))
    for i in second_note:
        print(binary_search(i,first_note))
