#Baekjoon 1662 압축.

## stack 이용해서 진행하면서 조건 만나면 수에 상관없이 (길이,연산자로 쓸 마지막 숫자)
## 만 stack에 더해주고 마지막으로 ')'를 만나면 다 빼주면서 연산해 최종 길이를 구할 수 있다.
to_ZIP = input()

stack = []
length = 0
last = ''

for i in range(len(to_ZIP)):
    if to_ZIP[i] == "(" :
        stack.append((length-1,last))
        length = 0
    elif to_ZIP[i] == ")" :
        pop_val = stack.pop()
        length = (length*int(pop_val[1]))+pop_val[0]
    else :
        length += 1
        last = to_ZIP[i]

print(length)