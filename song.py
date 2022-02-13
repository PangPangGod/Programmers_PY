
#[3차] 방금 그곡
#https://programmers.co.kr/learn/courses/30/lessons/17683

# 1차 시도(실패)
def solution(m, musicinfos):
    result = {}
    for i in musicinfos:
        temp = i.split(',')
        #시간 비교해서 차이 정리하기
        a = [*map(int,temp[1].split(':'))]
        b = [*map(int,temp[0].split(':'))]
        c = (a[0]-b[0])*60+a[1]-b[1]   ## 분단위 잘라서 저장, 시간이 큰 경우 *60해서 저장
        if len(temp[3]) > c and m in temp[3][:c] :
            result[temp[2]] = len(temp[3][:c])
        elif len(temp[3]) <= c and m in (temp[3]*(c//len(temp[3])))[:c] :
            result[temp[2]] = len((temp[3]*(c//len(temp[3])))[:c])
    
    result = sorted(result.items(),key = lambda x : x[1],reverse=True)
    if len(result) != 0 :
        return (result[0][0])
    else :
        return "(None)"

#2차 시도(성공)
def solution(m, musicinfos):
    def shap_to_lower(s):
        s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        return s
    m = shap_to_lower(m)
    result = []
    
    for i in musicinfos:
        temp = i.split(',')
        #시간 비교해서 차이 정리하기
        a = [*map(int,temp[1].split(':'))];b = [*map(int,temp[0].split(':'))]
        c = (a[0]-b[0])*60+a[1]-b[1]   ## 분단위 잘라서 저장, 시간이 큰 경우 *60해서 저장
        d = shap_to_lower(temp[3])
        d = d*(c//len(d))+d[:c%len(d)]
        song = temp[2]
        
        if m in d[:c] :
            result.append([song,len(d[:c])])
    
    if result:
        result = sorted(result, key = lambda x: (-x[1]))
        return result[0][0]
    else:
        return "(None)"
