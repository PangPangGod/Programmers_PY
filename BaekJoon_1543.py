finding = list(input())
answer = input()
temp = ''
ans = 0

for i in finding :
    temp += i
    if answer == temp[-len(answer):] :
        ans+=1
        temp = ''
print(ans)