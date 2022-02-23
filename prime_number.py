import math
def solution(n):
    answer = [True for _ in range(n+1)]
    answer[0]=False;answer[1] = False
    
    for i in range(2,n+1):
        if answer[i] == True :
            num = 2
            while (i*num) <= n:
                answer[i*num] = False
                num+=1
    storage = []
    for i in range(len(answer)):
        if answer[i] is True :
            storage.append(i)
    
    return len(storage)