import sys
input = sys.stdin.readline

N = int(input())
list_a=[]
list_a = list(map(int,input().split()))

M = int(input())
list_b=[]
list_b = list(map(int,input().split()))

dic = {}
for i in list_a :
    if i in dic :
        dic[i] += 1
    else :
        dic.setdefault(i,1)

for i in list_b :
    if i in dic :
        print(dic[i],end=' ')
    else :
        print(0,end=' ')