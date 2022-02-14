# 벌집(2292)
# https://www.acmicpc.net/problem/2292


def honeycomb(n):
    start = 1;end = 1;count = 1
    while True :
        if n not in range(start,end+1):
            start = end+1
            end = end+(6*count)
            count += 1
        else :
            break
    print(count)
    
# honeycomb(int(input()))

# n = int(input())
# cnt_num = 1
# cnt = 1
# while n > cnt_num:
#     cnt_num += 6*cnt
#     cnt+=1

# print(cnt)