#14888 연산자 끼워넣기(Backtracking)

#dictionary main에 사용해서 global 제거 완료.
#deepcopy도 제거 완료.
import sys

input = sys.stdin.readline

def calculation(storage,nums,operator_dict) :
    for i in range(1,len(nums)) :
        nums[i] = operator_dict[storage[i-1]](nums[i-1],nums[i])
    return nums[-1]

def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mul(a,b) :
    return a*b
def div(a,b) :
    if a < 0 :
        return (-a//b)*-1
    return a//b

def backtrack(depth,storage,nums,operator_dict) :
    
    if depth == N-1 :
        nums_sample = nums[:]
        
        result = calculation(storage,nums_sample,operator_dict)
        result_dict['max_result'] = max(result_dict['max_result'],result)
        result_dict['min_result'] = min(result_dict['min_result'],result)

        return
    
    for i in range(4) :
        if operator_list[i] != 0:
            operator_list[i] -= 1

            temp.append(i)

            backtrack(depth+1,storage,nums,operator_dict)
            operator_list[i] += 1
            temp.pop()


#main
N = int(input())
nums = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

operator_dict = {0:add,1:sub,2:mul,3:div}


result_dict = {'max_result':-(sys.maxsize), 'min_result':sys.maxsize}

temp = []
backtrack(0,temp,nums,operator_dict)

print(int(result_dict['max_result']),int(result_dict['min_result']),sep='\n')