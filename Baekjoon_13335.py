#13335 트럭
#N : 다리를 건너는 트럭의 수
#W : 다리의 길이
#L : 다리의 최대하중
from collections import deque

N,W,L = map(int,input().split())
truck_weight = deque(list(map(int,input().split())))
bridge = deque([0 for _ in range(W)])
time = 0

while truck_weight :

    bridge.popleft()
    if sum(bridge)+truck_weight[0] <= L :
        bridge.append(truck_weight.popleft())
    else :
        bridge.append(0)
    time += 1    
    
print(time+W)
