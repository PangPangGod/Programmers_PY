# A와 B (12904)
# https://www.acmicpc.net/problem/12904
# destination to start

S=input();T=input()

while True :
    if T==S :
        print(1)
        break
    elif len(S) > len(T) :
        print(0)
        break
    
    if T[-1] == 'A' :
        T = T[:-1]
    else :
        T = T[:-1][::-1]