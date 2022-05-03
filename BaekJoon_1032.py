N = int(input())

strings = [input() for _ in range(N)]
answer = list(strings[0])
str_len = len(strings[0])
if N == 1 :
    print(strings[0])
else :
    for i in range(str_len) :
        for k in range(1,N):
            if strings[k][i] != answer[i]:
                answer[i] = '?'
                continue
    print(''.join(answer))
