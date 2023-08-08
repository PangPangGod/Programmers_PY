#Baekjoon 2346 풍선 터뜨리기

from collections import deque
num = int(input())
queue = deque(enumerate(map(int, input().split())))

answer = []

# print(queue)
while queue :
    index, balloon = queue.popleft()
    answer.append(index+1)

    if balloon > 0 :
        queue.rotate(-(balloon-1))
    else :
        queue.rotate(-balloon)

print(*answer)