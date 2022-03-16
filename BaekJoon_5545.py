#최고의 피자 5545
#https://www.acmicpc.net/problem/5545
#일단 도우만 있을 때 1원당 열량만 출력
#그리디하게 해당 경우를 base 삼아서 max한 값만 받는다
#수학적으로 생각해 보았을 때, 가장 가격이 높은 경우부터 더해주는게 가장 큰 열량 당 가격을 구하는 방법이다.

N = int(input())
dough_price,topping_price = map(int,input().split())
dough_kcal = int(input())
topping_kcal = [int(input()) for i in range(N)]
topping_kcal.sort(reverse=True)

base_one = dough_kcal//dough_price

for i in range(len(topping_kcal)):
    price = dough_price + topping_price*(i+1)
    kcal = sum(topping_kcal[:i+1])
    base_one = max(base_one,(dough_kcal+kcal)//price)
    
print(base_one)