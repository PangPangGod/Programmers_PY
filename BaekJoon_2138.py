#전구와 스위치 2138
#https://www.acmicpc.net/problem/2138

N = int(input())
def start_branch_1(start):
    count=0
    for i in range(1,N):
        if start[i-1] != end[i-1] :
            count +=1
            start[i-1] = int(not start[i-1])
            start[i] = int(not start[i])
            if i != N-1 :
                start[i+1] = int(not start[i+1])
    if start == end :
        return count
    else :
        return -1

def start_branch_2(start):
    count=1
    start[0] = int(not start[0])
    start[1] = int(not start[1])
    for i in range(1,N):
        if start[i-1] != end[i-1] :
            count +=1
            start[i-1] = int(not start[i-1])
            start[i] = int(not start[i])
            if i != N-1 :
                start[i+1] = int(not start[i+1])
    if start == end :
        return count
    else :
        return -1

start=list(map(int,input()))
end=list(map(int,input()))

branch_1 = start_branch_1(start[:])
branch_2 = start_branch_2(start[:])

if branch_1>=0 and branch_2>=0:
    print(min(branch_1,branch_2))
elif branch_1>=0 and branch_2<0 :
    print(branch_1)
elif branch_2>=0 and branch_1<0 :
    print(branch_2)
else :
    print(-1)
