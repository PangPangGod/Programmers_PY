### 튜플
#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = set()
    result = []
    s = s[2:-2].split('},{')
    s.sort(key= lambda x : len(x))
    
    for i in s :
        temp = set(list(map(int,i.split(','))))
        result += list(set.difference(temp, answer))
        answer = temp
    
    return result