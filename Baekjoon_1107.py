# Baekjoon 1107 리모콘 ->
# 해결 코드

# 너무 복잡하게 여러 조건을 거니까 연산이 안돼서 그냥 완전탐색함...
# 즉 0부터 100만까지 돌면서 가장 적게 누르는 수를 구해서 연산 완료했다.
# 시간복잡도 이게 왜 낮음?
#stopword에 있는지 체크함

def get_turn(num,stopword) :
    flag = True
    num_lst = list(map(int,list(str(num))))
    for i in num_lst :
        if i in stopword :
            flag = False

    return flag

#main
num = int(input())
N = int(input())
if N != 0 :
    stopword = list(map(int,input().split()))
else :
    stopword = []

#기준점 100에서부터 해당 수(num)까지 -혹은 + 눌러서 가는 경우.
answer = abs(num-100)
for i in range(1000001) :
    if get_turn(i,stopword) :
        answer = min(answer,abs(num-i)+len(str(i)))
print(answer)