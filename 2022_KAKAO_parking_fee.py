import math
def solution(fees, records):
    _list = []
    case = set()
    for i in records :
        a,b,c=map(str,i.split())
        _list.append((a,b,c))
        case.add(b)
    
    car_dict = {}
    for i in case :
        car_dict[i] = 0
        
    inn = []
    outt = []
    
    for i in case :
        for j in _list :
            if j[1] == i and j[2] == 'IN':
                a,b = map(int,j[0].split(':'))
                inn.append((a,b))
            elif j[1] == i and j[2] == 'OUT':
                a,b = map(int,j[0].split(':'))
                outt.append((a,b))
        if len(inn) > len(outt):
            outt.append((23, 59))
        for k in range(len(inn)):
            if outt[k][1]-inn[k][1] < 0 :
                car_dict[i]+=(outt[k][0]-inn[k][0]-1)*60+outt[k][1]+60-inn[k][1]
            else :
                car_dict[i]+=(outt[k][0]-inn[k][0])*60+outt[k][1]-inn[k][1]
        inn = []
        outt = []
    
    sorted_car_dict = sorted(car_dict.items(),key=lambda x:x[0])
    print(sorted_car_dict)
    answer = []
    for i in sorted_car_dict:
        if i[1] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((i[1]-fees[0])/fees[2])*fees[3])
        
    return answer