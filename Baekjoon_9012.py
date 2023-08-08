
# Baekjoon 9012 괄호
#########################

#전체적으로 함수 쓰고, 좀 더 깔끔하게 푸는것에 집중한듯.
#로직은 한달 전과 생각하는데 크게 달라지지 않은 것 같다. 오히려 문제가 쉬워서 그런듯?
#괜찮다.

####### 옛날 풀이 ########

bracket_num = int(input())
stack = []

for j in range(bracket_num) :
    stack = []
    bracket = input()
    for k in bracket :

        if k == "(" :
            stack.append(k)
        
        else :
            if len(stack) == 0  :
                stack = ['NO']
                break
            else :
                stack.pop()

    if len(stack) == 0 : print('YES')
    else : print("NO")

################################################################################

# import sys

# def parenthesis_classifier(parenthesis) :
#     stack = []

#     for part in parenthesis :
#         if part == "(" :
#             stack.append(0)
#         else :
#             if not stack :
#                 return "NO"
#             else :
#                 stack.pop()

#     if stack :
#         return "NO"
#     return "YES"

################################################################################

# num = sys.stdin.readline()

# for _ in range(int(num)) :
#     print(parenthesis_classifier(input()))

# import sys

# def parenthesis_classifier(parenthesis) :
#     stack = []

#     while '()' in parenthesis :
#         parenthesis = parenthesis.replace("()","")

#     if parenthesis :
#         print("NO")
#     else :
#         print("YES")
#     return

# num = sys.stdin.readline()

# for _ in range(int(num)) :
#     parenthesis_classifier(sys.stdin.readline().rstrip())