#Baekjoon 10971 외판원 2

#시간복잡도 순열 돌려서 오래 걸림..
#모든 순열을 구한 후에 해당 조합으로 타고 들어가서 제일 적은 수를 구하는 BruteForce 방식
N = int(input())
path = []
storage = []
temp = []
used = [0 for i in range(N)]

for i in range(N) :
    path.append(list(map(int, input().split())))

def track(arr,path) :
    result = 0
    for i in range(N):
        if path[arr[i-1]][arr[i]] == 0 :
            result += 40000000
            continue
        result+=(path[arr[i-1]][arr[i]])
    return result

def backtrack(limit) :
    if len(temp) == limit :
        storage.append(track(temp,path))
        return

    for i in range(0,N) :
        if not used[i] :
            temp.append(i)
            used[i] = 1
            backtrack(limit)
            used[i] = 0
            temp.pop()

backtrack(N)
print(min(storage))
