#Baekjoon 15686 치킨 배달

#치킨 절단 완료

#combinations 이용하지 않고 구현해서 시도했으나 시간이슈로 인해 itertools에게 굴복해버렸다.
#기본적인 개념은 모든 치킨집중 살아남아야 하는 치킨집의 개수의 조합을 만들었다.
#그리고 이러한 조합에 대해 모든 집의 치킨 거리를 구하고 이를 통해 도시의 치킨 거리를 구한 뒤 최솟값을 찾았다.

import sys
from itertools import combinations

input = sys.stdin.readline

N,chicken_survive = map(int,input().split())
alley = [list(map(int,input().split())) for i in range(N)]

chicken_coord = []
house_coord = []

for i in range(N):
    for k in range(N):
        if alley[i][k] == 1 :
            house_coord.append([i,k])
        if alley[i][k] == 2 :
            chicken_coord.append([i,k])

result = sys.maxsize

for chi in combinations(chicken_coord,chicken_survive):  
    store = 0            
    for h in house_coord: 
        chi_len = 999   
        for j in range(chicken_survive):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        store += chi_len
    result = min(result, store)

print(result)


# import sys
# input = sys.stdin.readline

# combination = []
# def backtrack_d(limit,arr,start,temp) :
#     global combination
#     if len(temp) == limit :
#         combination.append(temp[:])
#         return
    
#     for i in range(start,len(arr)):
#         if arr[i] not in temp :
#             temp.append(arr[i])
#             backtrack_d(limit,arr,start+1,temp)
#             temp.pop()

# N,chicken_survive = map(int,input().split())
# alley = [list(map(int,input().split())) for i in range(N)]

# chicken_coord = []
# house_coord = []


# for i in range(N):
#     for k in range(N):
#         if alley[i][k] == 1 :
#             house_coord.append([i,k])
#         if alley[i][k] == 2 :
#             chicken_coord.append([i,k])

# backtrack_d(chicken_survive,chicken_coord,0,[])
# result = sys.maxsize

# for chi in combination:  
#     store = 0            
#     for h in house_coord: 
#         chi_len = 999   
#         for j in range(chicken_survive):
#             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
#         store += chi_len
#     result = min(result, store)

# print(result)
