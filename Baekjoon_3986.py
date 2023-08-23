#Baekjoon 3986 좋은 단어
import sys

def run() :
    stack = []
    word = list(sys.stdin.readline().rstrip())

    while word:
        temp = word.pop()
        if not stack or temp != stack[-1] :
            stack.append(temp)
        else :
            stack.pop()
            
    if stack :
        return 0
    return 1

#main 
answer = 0

for _ in range(int(sys.stdin.readline())) :
    answer += run()
print(answer)