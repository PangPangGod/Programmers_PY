# 블랙잭 2798
# https://www.acmicpc.net/problem/2798

from itertools import combinations
import sys
input = sys.stdin.readline
N,target=map(int,input().split())
numbers = list(map(int,input().split()))

target_list = [*combinations(numbers,3)]
temp = []
for i in target_list :
    sum_i = sum(i)
    if sum_i > target :
        continue
    else :
        temp.append(sum_i)
temp.sort(reverse=True)
print(temp[0])