# 1021 회전하는 큐

from collections import deque
import sys

def idx_check(queue,target_num) :
    idx_target = queue.index(target_num)

    if idx_target > len(queue)//2 :
        return len(queue)-idx_target
    else :
        return -idx_target
    
#main

deq_size, target_size = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1,deq_size+1)])
target = deque(list(map(int,input().split())))

counter = 0

while target :
    if queue[0] == target[0] :
        queue.popleft()
        target.popleft()

    else :
        tg = target.popleft()

        rotation = idx_check(queue,tg)
        queue.rotate(rotation)

        counter += abs(rotation)
        queue.popleft()

print(counter)