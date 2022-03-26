from itertools import combinations
import sys
answer = []
heights = [int(input()) for _ in range(9)]
heights.sort()
heights = list(combinations(heights,7))
for i in heights :
    if sum(i) == 100 :
        answer = i
        break
    
for i in answer :
    print(i)