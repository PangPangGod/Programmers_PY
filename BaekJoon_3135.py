#https://www.acmicpc.net/problem/3135
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
N=int(input())

bookmark = [int(input()) for _ in range(N)]
button = 0
manual = abs(A-B)

for i in range(N):
    bookmark[i] = abs(bookmark[i]-B)+1
bookmark.append(manual)
print(min(bookmark))

