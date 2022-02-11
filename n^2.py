# n^2
# https://programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    result = []
    for i in range(int(left),int(right+1)):
        num1 = i//n
        num2 = i%n
        if num2>num1 : num1,num2 = num2,num1
        result.append(num1+1)
    return result