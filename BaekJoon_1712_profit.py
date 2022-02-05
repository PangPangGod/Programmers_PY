# 1712
# https://www.acmicpc.net/problem/1712

fixed_cost,variable_cost,income=map(int,input().split())

if variable_cost >= income :
    print(-1)
else :
    profit = income - variable_cost
    print((fixed_cost//profit)+1)
