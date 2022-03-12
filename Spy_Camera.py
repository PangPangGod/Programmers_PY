#단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3


# 결론
# 카메라는 먼저진출한지점 순서대로 설치되어야한다.
# 예외

# 차량의 진입위치가 설치된 카메라보다 앞이라면, 카메라를 지나치므로 카메라의 추가적인 설치가 필요없다.

def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    current_camera = -30001
    for i in routes :
        if i[0] > current_camera :
            answer += 1
            current_camera = i[1]
    return answer