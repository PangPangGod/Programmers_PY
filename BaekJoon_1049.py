#1049 기타줄
#N이 끊어진 기타줄 개수, M이 브랜드
import math
N,M = map(int,input().split())
sep = []
package = []

for i in range(M):
    cost1,cost2=map(int,input().split())
    package.append(cost1)
    sep.append(cost2)

pack_min = min(package);sep_min = min(sep)
print(min(math.ceil(N/6)*pack_min,((N//6)*pack_min)+(N%6*sep_min),N*sep_min))