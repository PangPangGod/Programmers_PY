#캐시
#https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
from collections import deque
def solution(cacheSize, cities):
    time = 0
    q = deque()
    
    if cacheSize == 0 :
        return len(cities) * 5
    else :
        for i in cities :
            i = i.upper()
            if i not in q:
                if len(q) == cacheSize:
                    time += 5
                    q.popleft()
                    q.append(i)
                elif len(q) < cacheSize :
                    time += 5
                    q.append(i)
            elif i in q :
                q.remove(i)
                q.append(i)
                time += 1
        return time