#########################################################################
#Baekjoon 1018 체스판 다시 칠하기
#https://www.acmicpc.net/problem/1018

#8,8 사각형이 옮겨다니면서 (0,0)에 있는 수에 따라 칠하기 해보면서 최소의 수를 구하는 방식으로 구현.
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

painting_count = []
square = []
for i in range(N) :
    square.append(list(input()))

for i in range(N-7):
    for k in range(M-7):
        paint_w = 0
        paint_b = 0

        for d in range(i,i+8) :
            for f in range(k,k+8) :
                if (d+f)%2 == 0 : #짝수일 때
                    if square[d][f] != 'W' :
                        paint_w += 1
                    if square[d][f] != 'B' :
                        paint_b += 1
                else :
                    if square[d][f] != 'W' :
                        paint_b += 1
                    if square[d][f] != 'B' :
                        paint_w += 1
        painting_count.append(paint_w)
        painting_count.append(paint_b)

print(min(painting_count))