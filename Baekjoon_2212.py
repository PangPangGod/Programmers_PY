#Baekjoon 2212(Greedy)

#사실 개념까지는 맞았다.
#각 노드별로 나오는 거리를 빼주고 이를 통해 어디에 넣느냐에 따라 최소/최대를 구하는 문제라고 생각했다.

#내 경우에는 최대 거리만 더해서 그리디하게 진행했는데
#이건 틀린거였고 다시 생각해보니까 최대에서 node-1번만큼 나눈 
#그룹 node개가 최소가 되면 된다....

#행복유치원 문제 풀어보면 그리디 최소 노드는 더 정확하게 알 수 있을듯.

N = int(input())
node = int(input())
highway = list(map(int,input().split()))

if node >= N :
    print(0)

else :
    highway = sorted(highway)

    highway_diff = [0 for i in range(len(highway)-1)]

    for i in range(1,len(highway)):
        highway_diff[i-1] = highway[i]-highway[i-1]
    highway_diff.sort()

    #node 그룹 수 만큼 node-1번 나눌 수 있다. 
    for _ in range(node-1) :
        highway_diff.pop()

    result = sum(highway_diff)

    print(result)