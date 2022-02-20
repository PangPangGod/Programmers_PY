#124나라의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = []
    while n>0:
        if n%3 == 0 :
            answer.append('4')
            n = (n//3)-1
        else :
            answer.append(str(n%3))
            n = n//3
    return ''.join(answer[::-1])