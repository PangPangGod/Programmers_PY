#프로그래머스 2단계 프린터
#https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    listed = [*enumerate(priorities)]
    answer = 0
    
    while True :
        popped = listed.pop(0)
        if any(popped[1] < i[1] for i in listed):
            listed.append(popped)
        else :
            answer += 1
            if popped[0] == location:
                break
    return answer

## any 함수를 사용해서 하나라도 큰 게 있으면 뒤에 넣는 큐 방식을 이용했고,(사실 pop(0)보다 popleft()사용하는게 더 낫다.)
## 만약 any 조건에 걸리지 않는 가장 큰 value를 가진 tuple이라면, answer += 1 했다.