# UCPC는 무엇의 약자일까? (15904)
# https://www.acmicpc.net/problem/15904
from collections import deque
temp = deque([i for i in ''.join(input().split()) if i.isupper()])

goal = 'UCPC'
result = ''
i = 0
while temp :
    current = temp.popleft()
    if current == goal[i] :
        result += goal[i]
        i += 1
    if result == 'UCPC':
        break

if result == 'UCPC' :
    print('I love UCPC')
else :
    print('I hate UCPC')
    
# 다른사람 풀이
# 나처럼 deque에서 하나씩 끄집어 낸게 아니라 문자열 자르기를 통해 해당 문자가 나온 곳까지 자르고 맞다면 더해서 조건과 일차하는지 구하였다.
# string = input()

# list1 = ['U', 'C', 'P', 'C']
# cnt = 0
# for i in range(len(list1)):
#     if list1[i] in string:
#         index = string.find(list1[i])
#         string = string[index:]
#         cnt += 1

# if cnt == 4:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

# A → B 16953

# a = 100 ; b = 40021

# global count
# count = 0