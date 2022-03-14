#5와 6의 차이 2864
#https://www.acmicpc.net/problem/2864

hello = list(input().split())

min_result=[]
max_result=[]

for k in hello :
    temp1 = ''
    temp2 = ''
    for i in k :
        if i == '5' or i == '6':
            temp1 += '5'
            temp2 += '6'
        else :
            temp1 += i
            temp2 += i
    min_result.append(int(temp1))
    max_result.append(int(temp2))

print(sum(min_result),sum(max_result))