#최댓값과 최솟값
#https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    a = [*map(int,s.split())]
    a.sort()
    answer += f'{a[0]} {a[-1]}'
    return answer
