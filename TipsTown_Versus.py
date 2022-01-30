####예상 대진표
#https://programmers.co.kr/learn/courses/30/lessons/12985
import math
def solution(n,a,b):
    count = 0
    while a!=b :
        a,b = math.ceil(a/2),math.ceil(b/2)
        count+=1
        
    return count