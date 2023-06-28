#Yonsei TOTO 12018
#이분탐색으로 시간 줄이기??


def merge_sort(lst) :
    if len(lst) < 2 :
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)
    
def merge(left,right) :
    sort_complete = []
    left_i, right_i = 0,0

    while len(left) > left_i and len(right) > right_i :
        if left[left_i] > right[right_i] :
            sort_complete.append(right[right_i])
            right_i += 1
        else :
            sort_complete.append(left[left_i])
            left_i += 1
    
    while len(left) > left_i :
        sort_complete.append(left[left_i])
        left_i += 1
    
    while len(right) > right_i :
        sort_complete.append(right[right_i])
        right_i += 1
    
    return sort_complete



class_num, my_milage = map(int,input().split())

result = 0
milages = []


for i in range(class_num) :
    attender, limit = map(int,input().split())
    milage_per_person = list(map(int,input().split()))

    #mergesort 돌려서 순서대로 만든 다음에 자르기
    milage_per_person = merge_sort(milage_per_person)
    if limit > attender :
        milages.append(1)
    else :
        milage_per_person = milage_per_person[::-1]
        milages.append(milage_per_person[limit-1])

for i in sorted(milages) :
    if my_milage - i >= 0 :
        result += 1
        my_milage -= i

print(result)