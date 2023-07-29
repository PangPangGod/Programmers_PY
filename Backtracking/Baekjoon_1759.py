#1759 암호 만들기(backtrack -> not combinations)

#backtrack 구현해서 푼 풀이.

N,M = map(int,input().split())
key_words = sorted(list(input().split()))
# ['a','e','i','o','u']

def V_C_word(word) :
    V = 0 #모음
    C = 0 #자음
    for i in word :
        if i not in ['a','e','i','o','u'] :
            C += 1
        else :
            V += 1
    return V,C

word = []

def backtrack(key_words,x) :
    if len(word) == N :
        V, C = V_C_word(word)
        if  V >= 1 and C >= 2 :
            print(''.join(word))
            return
    
    for i in range(x,M) :
        if key_words[i] not in word :
            word.append(key_words[i])
            backtrack(key_words,i)
            word.pop()

backtrack(key_words,0)

######################################################################

#combinations 쓴 풀이.

from itertools import combinations

N,M = map(int,input().split())
key_words = sorted(list(input().split()))
# ['a','e','i','o','u']

def V_C_word(word) :
    V = 0 #모음
    C = 0 #자음
    for i in word :
        if i not in ['a','e','i','o','u'] :
            C += 1
        else :
            V += 1
    return V,C

for word in list(combinations(key_words, N)) :
    V, C = V_C_word(word)

    if  V >= 1 and C >= 2 :
        print(''.join(word))
