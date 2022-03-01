# 통나무 뛰어넘기 11497
#https://www.acmicpc.net/problem/11497
from sys import stdin


t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    heights = [int(x) for x in stdin.readline().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)
          
# from collections import deque
# N = int(input())
# last = []
# for _ in range(N):
#     leng = int(input())
#     sample = [*map(int,input().split())]
#     sample.sort(reverse=True)

#     sample = deque(sample)
#     answer = deque()

#     #deque 이용해 정규분포 만들기
#     i = 0
#     while sample :
#         current = sample.popleft()
#         if i == 0 :
#             answer.append(current)
#         elif i%2 == 1 :
#             answer.append(current)
#         else:
#             answer.appendleft(current)
#         i+=1

#     #정규분포 중 최댓값 출력
#     max_num = 0
#     for k in range(1,leng):
#         if k == leng-1 :
#             max_num = max(max_num,answer[-1]-answer[0])
#         else :
#             max_num = max(max_num,answer[k]-answer[k-1])
#     last.append(max_num)

# for i in last :
#     print(i)