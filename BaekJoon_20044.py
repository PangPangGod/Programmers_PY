#Project Team 20044
#https://www.acmicpc.net/problem/20044

team_num = int(input())
teams = [0]+list(map(int,input().split()))
teams.sort()

answer = teams[1]+teams[-1]
for i in range(1,team_num+1):
    answer=min(answer,teams[i]+teams[-i])
print(answer)