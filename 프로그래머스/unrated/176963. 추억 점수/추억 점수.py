def solution(name, yearning, photo):
    dic = {}
    for i, n in enumerate(name):
        dic[n] = yearning[i]
        
    answer = []
    
    for p in photo:
        tot = 0
        for ppl in p:
            if ppl in dic:
                tot += dic[ppl]
            
        answer.append(tot)
    return answer