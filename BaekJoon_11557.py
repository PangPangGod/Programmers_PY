#Yangjojang of The Year(11557)
#https://www.acmicpc.net/problem/11557
temp = 0
temp_name = ''
storage = []
T = int(input())
for i in range(T):
    N = int(input())
    for i in range(N):
        a,b = input().split()
        b = int(b)
        temp = max(temp,b)
        if temp == b :
            temp_name = a
    storage.append(temp_name)
[print(i) for i in storage]