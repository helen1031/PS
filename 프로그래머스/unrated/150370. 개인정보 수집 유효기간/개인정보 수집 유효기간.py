def convertDate(year, month, day, duration):
    endy = year
    endm = month + duration
    endd = day
    
    enddate = endy * 12 * 28 + endm * 28 + endd
        
    return enddate

def solution(today, terms, privacies):    
    # 전처리
    tyear, tmonth, tday = map(int, today.split("."))
    todaydate = tyear * 12 * 28 + tmonth * 28 + tday
    
    tdict = {}
    for term in terms:
        alpha, month = map(str, term.split())
        tdict[alpha] = int(month)
        
    answer = []
    
    for i, privacy in enumerate(privacies):
        date, term = map(str, privacy.split())
        y, m, d = map(int, date.split("."))
        
        enddate = convertDate(y, m, d, tdict[term])
        
        if todaydate >= enddate:
            answer.append(i + 1)
    
    return answer