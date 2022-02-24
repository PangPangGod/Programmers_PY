#유기농 배추 DFS (1012)
#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def selector(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    if graph[x][y] == 1 :
        graph[x][y] = 0
        selector(x-1,y)
        selector(x+1,y)
        selector(x,y-1)
        selector(x,y+1)
        return True
    
    return False

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    result = 0

    for _ in range(K):
        y,x = map(int,input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if selector(i,j) :
                result += 1
        
    print(result)