#욱제는 효도쟁이야
#https://www.acmicpc.net/problem/11487
N = int(input())
towns = list(map(int,input().split()))
print(sum(towns)-max(towns))