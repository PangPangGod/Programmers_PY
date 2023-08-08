#백준 10799 쇠막대

# ()는 레이저 표현
# (    )는 쇠막대기 표현.
# 따라서 기본적인 아이디어는 )를 만났을 때 전 괄호를 체크해서 ()가 완성되면 레이저, ((이면 파이프 하나로 취급.

forge = input()

# forge = '(((()(()()))(())()))(()())'
stack = []

counter = 0
for idx in range(len(forge)) :
    # print(stack)

    if forge[idx] == "(" :
        stack.append("(")
    
    else :
        stack.pop()

        if forge[idx-1] == "(" :
            counter += len(stack)
        else :
            counter += 1

print(counter)