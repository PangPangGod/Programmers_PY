#10250
#https://www.acmicpc.net/problem/10250

N = int(input())
result = []
for _ in range(N):
    height,width,cust_no = map(int,input().split())
    first = cust_no%height
    second = cust_no//height+1
    
    if first == 0 :
        first = height
        second -= 1
    if second < 10 :
        result.append(str(first)+'0'+str(second))
    else :
        result.append(str(first)+str(second))
for i in result:
    print(int(i))