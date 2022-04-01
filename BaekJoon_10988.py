#10988 팰린드롬인지 확인하기
#https://www.acmicpc.net/problem/10988

word = list(input())
N = len(word)//2
status = 1
for i in range(N) :
    if word[i] != word[-(i+1)] :
        status = 0
        break
print(status)
