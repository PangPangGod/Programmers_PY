# Baekjoon 1068 트리.

N = int(input())

# 기본 아이디어는 이어지는 tree를 일종의 인접 리스트로 만들어서 2차원 배열에 나열하였다. list의 index는 노드의 숫자이고, 
# 내부에 있는 수들은 이어지는 노드에 해당한다. 만약 해당 리스트가 비어있으면 더 이상 갈 곳이 없는 것.
def draw_node(N) :
    temp = [[] for i in range(N)]
    root = []
    depth_list = list(map(int, input().split()))
    for i in range(len(depth_list)):
        if depth_list[i] == -1 :
            root.append(i)
        
        else :
            temp[depth_list[i]].append(i)
    
    return temp,root

result,root = draw_node(N)
stop_word = int(input())
leaf = 0

def depth_search(num,origin) :
    global leaf

    # 중단 조건 : num이 stop_word와 같을 때, 더 이상 들어갈 node가 없을 때(leaf +1)
    # 이 때 고려해야 하는 경우가 만약 해당 num이 들어가기 전인 origin 노드의 길이가 1이라면
    # 이어지는 노드가 중단점이라고 그냥 return 해버리면 해당 origin이 leaf가 되는 경우를 제외하므로
    # 이를 체크해서 꼼수로 num = []로 설정한 다음에 바로 leaf 더하고 return 해버리는 형식으로 넘겼다. (어짜피 origin의 len이 1이라면 중단점 이후에 이어지는 노드가 없으므로.)

    # 더 깔끔하게 푸는법이 있나??
    if num == stop_word :
        if len(result[origin]) == 1 :
            result[num] = []
        else :
            return

    #받은 노드의 리스트가 비었다면 leaf로 간주, 추가 후 return.    
    if result[num] == [] :
        leaf += 1
        return
    
    for i in result[num] :
        depth_search(i,num)


#root가 여러개일 경우 고려해서 만든 실행문, origin의 경우에는 시작 수와 동일하게 주었더니 오류가 없었다.
for i in root :
    depth_search(i,i)

#출력
print(leaf)