#Baekjoon 10546 배부른 마라토너

#시간복잡도는 set랑 dictionary 조합해서 했던데
#이건 좀 별로인듯??
import sys

def run(num) :
    storage = {}
    for _ in range(num) :
        if storage.get((name:=sys.stdin.readline().rstrip())) :
            storage[name] += 1
        else :
            storage[name] = 1
    
    for _ in range(num-1) :
        storage[sys.stdin.readline().rstrip()] -= 1

    for n in storage :
        if storage[n] :
            return n
        
print(run(int(sys.stdin.readline())))