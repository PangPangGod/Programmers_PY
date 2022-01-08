'''탐욕법(Greedy) 알고리즘 문제
한번에 최대 2명씩 밖에 탈 수 없는 구명보트, 무게 제한 존재
구명보트 개수의 최솟값을 return'''

# 나의 코드

def solution(people, limit):
    answer=0
    people.sort(reverse=True)
    
    for i in people :
        if (i+people[-1]) <= limit:
            answer += 1
            people.pop()
        else : answer += 1
    return answer

''' 처음에는 여러 조건을 통해 해결하려고 했는데, 효율성 오류나 정답이 인정되지 않아 고민했다.
단순하게 생각해서 for문을 통해 정렬한 people 리스트에서 하나씩 꺼낸 후,
만약 최솟값(정렬했으니 -1에 해당하는 인덱스)와 더했을 때 limit보다 작거나 같으면 두 사람이 탈 수 있다고 생각해
보트 1개를 더하고 최솟값만 pop해주면서 진행시켰다.
여기서 i에 대해서 pop을 진행하지 않은 이유는 OutofRange 오류도 있지만, 어짜피 for문을 통해 진행하고 조건에도 걸리지 않으므로 상관 없다고 생각했기 때문이다.

이외에도 전체 인원에서 짝지은 수만 빼주는 방식으로 보트의 수를 구하는 방식도 있다.
'''