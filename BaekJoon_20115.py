N = int(input())

drinks = list(map(int,input().split()))
drinks.sort(reverse=True)

while True :
    if len(drinks) == 1 :
        break
    temp=drinks.pop()
    drinks[0] += temp/2

print(drinks[0])