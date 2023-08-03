#Baekjoon 28278 스택 2
import sys
input = sys.stdin.readline

stack = []

def add(x) :
    stack.append(x)

def stack_pop() :
    if stack :
        print(stack.pop())
    else :
        print(-1)

def stack_print() :
    print(len(stack))

def stack_check() :
    if stack :
        print(0)
    else : print(1)
def stack_check_print() :
    if stack :
        print(stack[-1])
    else :
        print(-1)

stack_funcs = {}

stack_funcs[1] = add
stack_funcs[2] = stack_pop
stack_funcs[3] = stack_print
stack_funcs[4] = stack_check
stack_funcs[5] = stack_check_print
    
for _ in range(int(input())) :
    cmd_lst = list(map(int, input().split()))

    if cmd_lst[0] == 1:
        stack_funcs[cmd_lst[0]](cmd_lst[1])
    else :
        stack_funcs[cmd_lst[0]]()