import heapq

def solution(operations):
    minq = []
    maxq = []
    
    length = 0
    for operation in operations:
        oper, num = operation.split(" ")
        
        if oper == "I":
            length += 1
            heapq.heappush(minq, int(num))
            heapq.heappush(maxq, -int(num))
        else:
            if length == 0:
                continue
            if num == "-1":
                length -= 1
                heapq.heappop(minq)
            else:
                length -= 1
                heapq.heappop(maxq)
    
    if length != 0:
        q = []
        while minq and maxq:
            num = heapq.heappop(minq)
            if -num in maxq:
                q.append(num)
                
        return [max(q), min(q)]
    
    else:
        return [0, 0]
    