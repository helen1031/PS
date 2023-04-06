import heapq

def solution(k, tangerine):
    
    tdic = {}
    for tan in tangerine:
        if tan in tdic:
            tdic[tan] += 1
        else:
            tdic[tan] = 1
    
    hq = []
    for key, value in tdic.items():
        heapq.heappush(hq, [value, key])
    
    remove = len(tangerine) - k
    while remove:
        targetv, targetk = heapq.heappop(hq)
        
        if targetv <= remove:
            remove -= targetv
        else:
            heapq.heappush(hq, [targetv - remove, targetk])
            remove = 0
    
    return len(hq)