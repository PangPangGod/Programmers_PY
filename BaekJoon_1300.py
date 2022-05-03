#N^ 행렬에서 K번째 수는?
N = int(input())
K = int(input())

start = 1
end = K

while start <= end :
    tmp = 0
    mid = (start+end)//2
    for num in range(1,N+1) :
        tmp += min(mid//num,N)
    #tmp는 mid일때 구해지는 인덱스
    if tmp < K :
        start = mid+1
    else :
        end = mid-1
print(tmp)