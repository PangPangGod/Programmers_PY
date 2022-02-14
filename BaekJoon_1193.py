# 분수찾기(1193)
# https://www.acmicpc.net/problem/1193
# 내 원래 풀이 >>>
n = int(input())
temp = 0
i = 1

while n > temp :
    temp += i
    i += 1
    
diff = temp-n

if i%2 == 0 :
    print(f'{diff+1}/{i-diff-1}')
else :
    print(f'{i-diff-1}/{diff+1}')