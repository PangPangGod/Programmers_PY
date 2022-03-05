#국회의원 선거 1417
#https://www.acmicpc.net/problem/1417

N=int(input())
candidates = [int(input()) for _ in range(N)]
dasom=candidates[0]
candidates=candidates[1:]
candidates.sort(reverse=True)
result = 0
while True :
    if not candidates :
        break
    target = max(candidates)
    if dasom > target :
        break
    candidates[0] -= 1
    dasom += 1
    result += 1
    candidates.sort(reverse=True)
    
print(result)