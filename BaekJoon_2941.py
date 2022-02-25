#크로아티아 알파벳
#https://www.acmicpc.net/problem/2941

croatian = ['c=','c-','dz=','d-','lj','nj','s=','z=']

N = input()
answer = 0
temp = ''
for i in N :
    temp += i
    if len(temp)>1 and temp[-2:] in croatian:
        if temp[-3:] == 'dz=' :
            answer += len(temp)-2;temp = ''
        else :
            answer += len(temp)-1;temp = ''
answer += len(temp)

print(answer)

## 다른사람 불이
# 비슷한 알고리즘이지만 나는 하나하나 진행시켰다면 replace를 통해 손쉽게 작성했다.

# n = input()
# li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# count = 0
# for i in li:
# 	n = n.replace(i, "@")
# print(len(n))