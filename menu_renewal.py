'''코드 설계

최소 2가지 이상의 단품메뉴로 구성한 코스요리
최소 2명 이상의 손님으로부터 주문된 단품요리 조합

주문배열 orders
추가하고 싶은 갯수 course

오름차순 정렬해 return
원소에 저장된 문자열 또한 오름차순

메뉴 구성이 여러 개라면, 모두 담아 return
orders와 cours 매개변수는 return하는 배열의 길이가 1 이상이 되도록.

나는 dict로 풀었지만 counter를 사용해 깔끔하게 정렬하는 방식도 있음.'''

from itertools import combinations
def solution(orders, course):
    course_dict = {}
    answer=[]
    
    for course_num in course:
        for order in orders :
            
            order = ''.join(sorted(order))
            a=[*combinations(order,course_num)]
            
            for i in a :
                b=''.join(i)
                if b not in list(course_dict.keys()):
                    course_dict[b] = 1
                else : course_dict[b] += 1
                    
        if course_dict == {}:
            continue
        
        for key,value in course_dict.items():
            if value == 1 :
                continue
            elif value == max(course_dict.values()):
                answer.append(key)
        course_dict = {}
        
    answer.sort()
    return answer

