#이진 변환 반복하기
#https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    count = 0
    minus_zero = 0
    while True :
        minus_zero += s.count('0')
        s = s.count('1')
        s = str(bin(s)[2:])
        count+=1
        if s == '1' :
            break
    
        
    answer = [count,minus_zero]
    return answer