#프로그래머스 2단계 N개의 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    #최대공약수 구하기
    def calc(A,B):
        if B == 0:
            return A
        return calc(B,A%B)
    #pop해주기 위해 정렬하기
    arr.sort(reverse=True)
    
    while len(arr) > 1 : 
        arr1 = arr.pop()
        arr2 = arr.pop()
        arr.append(arr1*arr2//calc(arr2,arr1))
    
    return arr[0]