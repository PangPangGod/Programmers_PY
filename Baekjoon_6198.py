#6198 옥상 정원 꾸미기
import sys

buildings = []
stack = []

for _ in range(int(sys.stdin.readline())) :
    buildings.append(int(sys.stdin.readline()))

result = 0

for i in range(len(buildings)) :
    # print(stack)
    while stack and buildings[i] >= stack[-1] :
        stack.pop()
    
    # print(len(stack)-1)
    result += len(stack)
    stack.append(buildings[i])

print(result)

################################################################################

# # n,*h=map(int,open(0).read().split()) #여러 입력 한 번에 받을 때.
# N, *buildings = map(int,open(0).read().split()) #EOF 있어야 실행 중단됨..
# # print(N,buildings) 

# stack = []
# result = 0

# for height in buildings :
#     while stack and stack[-1] <= height :
#         stack.pop()
#     result += len(stack)
#     stack.append(height)

# print(result)