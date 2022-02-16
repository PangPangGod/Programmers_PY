#단어 변환 (DFS/BFS)
#https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    answer = 0
    checker = [0 for _ in range(len(words))]
    pops = [begin]
    
    if target not in words :
        return 0
    
    #단어 비교하는 함수 (알파벳 1개 차이날때만 True)
    def search_engine(begin,word):
        temp=0
        for i in range(len(word)) :
            if begin[i] == word[i]:
                temp+=1
        if temp == len(begin)-1 :
            return True
        return False
    
    while pops :
        current = pops.pop()
        if current == target :
            return answer
        for i in range(len(words)):
            if search_engine(current,words[i]) and checker[i] == 0 :
                checker[i] = 1
                pops.append(words[i])
        answer += 1 #차원 올리기
        
    return answer