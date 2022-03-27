#통계학 2108
#https://www.acmicpc.net/problem/2108
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
mean = round(sum(nums)/len(nums))
median = nums[len(nums)//2]

##최빈값 구해보자
mode = 0
count = Counter(nums).most_common(2)
if len(nums) == 1 :
    mode = count[0][0]
else :
    if count[0][1] == count[1][1] :
        mode = count[1][0]
    else :
        mode = count[0][0]
        
print(mean)
print(median)
print(mode)
print(max(nums)-min(nums))