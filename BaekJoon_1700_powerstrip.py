N,K = map(int,input().split())
schedule = list(map(int,input().split()))
current_status = []
sign=0

## 시작하기 전에 크게 세가지 과정을 전개했다.
## 1. 최우선으로 현재 사용할 도구가 멀티탭 내부에 있을 경우 -1로 처리 후 (3번에서 index 검색 시 중복 없애기 위해) pass
## 2. 그 다음으로 멀티탭에 들어갈 수 있는 개수 N보다 현재 멀티탭에 있는 도구의 개수가 적을 경우 append 후 -1로 처리
## 3. 멀티탭의 개수가 꽉 찼을 경우 (N == len(current_status))
## 3-1. 멀티탭의 개수가 꽉 찼는데 앞으로 사용하지 않을 도구가 꽂혀있는 경우 최우선으로 멀티탭에서 뽑고 break
## 3-2. 만약 schedule에 앞으로 사용할 도구가 있다면 그것들 중에 현재 schedule에서 가장 나중에 사용할 (0부터 schedule.index(j)까지의 거리가 최대인)
## 도구의 index를 찾은 후 loop가 종료되면 멀티탭에서 뽑는다.

for i in range(len(schedule)):
    if schedule[i] in current_status :
        schedule[i] = -1
        pass
    elif N > len(current_status):
        current_status.append(schedule[i])
        schedule[i] = -1
    elif N == len(current_status) :
        num = 0
        temp = 0
        max_j = 0
        index_j = 0
        for j in current_status:
            if j not in schedule :
                current_status.pop(current_status.index(j))
                current_status.append(schedule[i])
                schedule[i] = -1
                sign += 1
                index_j = -1
                break
            else :
                num = len(schedule[:schedule.index(j)])
                temp = max(num,max_j)

                if temp == num :
                    max_j = num
                    index_j = current_status.index(j)
        if index_j >= 0 :
            current_status.pop(index_j)
            current_status.append(schedule[i])
            schedule[i] = -1
            sign += 1
print(sign)