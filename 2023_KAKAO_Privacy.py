#2023 KAKAO BLIND RECRUIMENT
#기준일을 2000년으로 잡고 2000 - 28*12*year + 28*month + day 하면 나오지 
#깔끔하기보다는 가독성 있게

def year_count(date) :
    year, month, day = date.split(".")
    return (int(year)-2000)*28*12+int(month)*28+int(day)

def solution(today, terms, privacies):
    answer = []
    
    #오늘 날짜 계산
    today_count = year_count(today)
    
    #term 계산
    term_dict = {}
    for i in terms :
        code, month = i.split(" ")
        term_dict[code] = int(month)*28
    
    #privacies 계산
    for index in range(len(privacies)) :
        date, code = privacies[index].split(" ")
        
        if today_count >= year_count(date)+term_dict[code]  :
            answer.append(index+1)
    
    return answer
    
 
