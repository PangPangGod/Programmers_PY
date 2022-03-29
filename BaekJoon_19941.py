#햄버거 분배 19941
#https://www.acmicpc.net/problem/19941

#식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
#햄버거를 먹을 수 있는 사람의 최대 수
#왼쪽부터 오른쪽까지 K번째 떨어진 곳 까지 햄버거가 존재하면 넣는다.
#왼쪽부터 찾는 이유는 마지막 사람은 무조건 왼쪽에서 찾아야 하기 때문이다.
n,k = map(int,input().split())
sample = list(input())
people = 0
for i in range(n):
    if sample[i] == 'P' :
        for v in range(max(i-k,0),min(i+k+1,n)):
            if sample[v] == 'H' :
                sample[v] = 0
                people += 1
                break
print(people)