#승률 구하기

X,Y = map(int,input().split())

#승률 구하기
# print(int(Y*100/X))

#0을 start로, X를 end로 해서 둘이 같다면 -1을 리턴하고,
#최소값을 만족할 때, 즉 lower bound일 때를 return하면 된다.

start = 1
end = X
answer = 0
bound = int(Y*100/X)+1
    

while start <= end :
    if bound > 99 :
        answer = -1
        break
    mid = (start+end)//2
    new_avg = int((Y+mid)*100/(X+mid))
    if new_avg<bound :
        start = mid+1
    else :
        end = mid-1
        answer = mid
print(answer)

