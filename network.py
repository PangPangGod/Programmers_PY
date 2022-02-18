#네트워크
#https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
def solution(n, computers):
    connection = [False for _ in range(n)]
    answer = 0
    
    def dfs(num) :
        if connection[num] == True :
            return
        connection[num] = True
        for i in range(n) :
            if num != i and connection[i] == False and computers[num][i] == 1 :
                dfs(i)
    
    while True :
        if False in connection :
            dfs(connection.index(False))
            answer += 1
        else :
            break
            
    return answer