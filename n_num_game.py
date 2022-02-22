#[3차]n진수 게임
#https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    global storage
    storage = ['0']
    answer = ''
    
    def selector(iter):
        iter = iter[::-1]
        global storage
        storage += list(iter)
    
    def digit(t,n):
        num_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        temp = ''
        while t>0:
            t,mod = divmod(t,n)
            if mod >= 10 :
                temp += num_dict[mod]
            else :
                temp += str(mod)
        return selector(temp)
        
    
    for i in range(1,t*m+1):
        digit(i,n)
    
    for k in range(p-1, t*m, m):
        answer += storage[k]
    
    return answer