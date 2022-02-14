# 부녀회장이 될테야(2775)
# https://www.acmicpc.net/problem/2775
#a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
def resident_num(floor,room):
    temp_floor = []
    temp_floor2 = []
    for i in range(floor+1):
        if i == 0 :
            temp_floor = [j+1 for j in range(room)]
        else :
            temp_floor2 = [sum(temp_floor[:k]) for k in range(1,len(temp_floor)+1)]
            
        if i == 0 :
            temp_floor2 = temp_floor
        else :
            temp_floor = temp_floor2
    return temp_floor[room-1]

# n = int(input())
# answer = []

# for i in range(n):
#     floor = int(input())
#     room = int(input())
#     answer.append(resident_num(floor,room))
    
# [print(k) for k in answer]