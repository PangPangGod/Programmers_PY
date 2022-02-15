#불량 사용자
#https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
from itertools import permutations
import re
def solution(user_id, banned_id):
    temp = []
    answer = 0
    count = 0
    permutation_list = [*permutations(user_id,len(banned_id))]
    banned_id = ['^'+i.replace('*','.')+'$' for i in banned_id]
    for i in range(len(permutation_list)):
        for j in range(len(banned_id)):
            if re.compile(banned_id[j]).match(permutation_list[i][j]):
                count += 1;pass
            else : break
        ab = sorted(list(permutation_list[i]))
        if count == len(banned_id) and ab not in temp:
            temp.append(ab)
            answer += 1    
        count=0

    return answer