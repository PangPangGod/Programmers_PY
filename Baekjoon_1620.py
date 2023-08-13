#1620 나는야 포켓몬 마스터 이다솜
import sys

poke_docs = {}
train,test = map(int,sys.stdin.readline().split())

for i in range(1,train+1) :
    poke_docs[(inp := sys.stdin.readline().rstrip())] = i
    poke_docs[str(i)] = inp

for _ in range(test) :
    print(poke_docs[(inp := sys.stdin.readline().rstrip())])