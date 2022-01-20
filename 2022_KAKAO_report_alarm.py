def solution(id_list, report, k):
    #report 중복 신고 제거
    report = list(set(report))
    answer = [0]*len(id_list)
    dic = {}
    
    for v in report:
        a,b = v.split()
        if b in dic.keys():
            dic[b]+=[id_list.index(a)]
        else:
            dic[b]=[id_list.index(a)]
    
    for i in dic.items():
        if len(i[1]) >= k :
            for j in i[1]:
                answer[j]+=1
                
    return answer
