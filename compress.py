#[3차] 압축
#https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    lst = [chr(x) for x in range(65, 91)]
    i = 0
    temp = msg[0]
    answer = []
    
    while i != len(msg) :
        if temp in lst :
            if i != len(msg)-1:
                i+=1
            else :
                answer.append(lst.index(temp)+1)
                break
            temp += msg[i]
        else:
            lst.append(temp)
            answer.append(lst.index(temp[:-1])+1)
            temp = msg[i]