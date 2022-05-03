import sys
input = sys.stdin.readline

N = int(input())
chemicals = list(map(int,input().split()))

left = 0
right = len(chemicals)-1
tmp = [abs(chemicals[left]+chemicals[right]),chemicals[left],chemicals[right]]
while left < right :
    ans = chemicals[left]+chemicals[right]
    if abs(ans)<tmp[0] :
        tmp[0]=abs(ans);tmp[1]=chemicals[left];tmp[2]=chemicals[right]
    if ans > 0 :
        right -= 1
    elif ans < 0 :
        left += 1
    else :
        break
print(tmp[1],tmp[2])