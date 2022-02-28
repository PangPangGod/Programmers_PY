# 캠핑 4796
# https://www.acmicpc.net/problem/4796

def camp_counter(L,P,V):
    a = V//P
    b = V%P
    if L == 0:
        return 0
    if L < b :
        b = L
    return (a*L)+b

hi = []
while True :
    L,P,V = map(int,input().split())
    if L == 0 and P == 0 and V == 0 :
        break
    hi.append(camp_counter(L,P,V))

for k in range(len(hi)) :
    print(f'Case {k+1}: {hi[k]}')
