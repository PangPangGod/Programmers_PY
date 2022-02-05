#백준 1789번 수들의 합
#https://www.acmicpc.net/problem/1789
'''
1부터 더해가면서 sum > s가 되는 순간 마지막으로 더한 숫자를 p라 하고, 

sum < s를 만족하는 최대의 sum을 sum2라 합시다.

sum2 == 1 + 2 +...+ p-1 < s

sum2 + p > s 이므로 s의 최대값은 sum2 + p - 1 입니다.

이때,  sum2에 더해진 1부터 p-1 까지의 수들을 큰 수 부터 1씩 증가시키면 더해진 숫자들은 겹치지 않고, sum2가 1씩 증가하게 됩니다.

이렇게 숫자들이 겹치지 않게 sum + 1부터 sum + (p-1)까지의 수를 구할 수 있습니다.'''
S = int(input())
result = 0
for i in range(1,4294967295):
    result += i
    if result > S :
        print(i-1)
        break