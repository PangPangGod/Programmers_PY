# Truck_on_Bridge
# https://programmers.co.kr/learn/courses/30/lessons/42583

# 큐를 통해 하나씩 집어넣으면서 sum을 이용하는 방식은 시간이 너무 오래 걸렸다.
# 따라서 current라는 변수에 현재 트럭 무게를 주고, 만약 무게를 넘으면 0을 통해 다리 길이만큼 밀어내고,
# 무게가 다리 무게보다 작다면 같이 더해서 다시 밀어내는 작업을 반복한다.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    current = 0
    
    while bridge :
        answer += 1
        current -= bridge.popleft()
        if truck_weights:
            if current + truck_weights[0] <= weight:
                current += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer