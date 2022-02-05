#백준 1541번
#https://www.acmicpc.net/problem/1541

#그리디하게 해결하는것보다 문자열 파싱을 통해 해결했다.
#최솟값을 구하기 위해서는 괄호를 -(부터 )- 가 나올 때 까지로 해석했다.
#따라서 -로 split 한 결과를 얻어내 괄호 안은 전부 더하면 되므로 부호를 없애고 전부 더했다.
#가장 처음과 마지막은 음수로 나온다고 적혀 있으므로, 첫번째는 무조건 양수로 설정하고 묶어진 다른 나머지는 무조건 음수로 설정해 더한 결과를 출력했다.

form = input()
f = form.split("-")
number = []
for i in range(len(f)) :
    temp = map(int,f[i].split("+"))
    if i == 0 :
        number.append(sum(temp))
    else :
        number.append(-sum(temp))
print(sum(number))
