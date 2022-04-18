first,last = map(int,input().split())
answer = 0

if len(str(first)) != len(str(last)):
    print(0)
else :
    first_1 = str(first)
    last_1 = str(last)
    if first_1[0] != last_1[0] :
        print(0)
    else :
        if first_1[0] == '8' :
            answer += 1
        for i in range(1, len(first_1)) :
            if first_1[i] != last_1[i]:
                break
            else :
                if first_1[i] == '8' :
                    answer += 1
        print(answer)