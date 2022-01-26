def solution(s):
    temp = []
    for i in range(1,len(s)//2+2):
        ans = ''
        cnt = 1
        for num in range(0,len(s),i):        
            if s[num:num+i] != s[num+i:num+i+i]:
                if cnt > 1 :
                    ans += str(cnt)+s[num:num+i]
                    cnt = 1
                else :
                    ans += s[num:num+i]
            else : cnt += 1
        temp.append(len(ans))
    
    return min(temp)

if __name__ == '__main__':
    solution("aabbacc")