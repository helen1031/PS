from collections import Counter

def solution(n, works):
    if sum(works) <= n :
        return 0
    
    counter = Counter(works)
    print(counter)
    
    while n > 0:
        maxnum, cnt = max(counter.items())
        del counter[maxnum]
        
        if n >= cnt:
            n -= cnt
            if maxnum - 1 in counter:
                counter[maxnum-1] += cnt
            else:
                counter[maxnum-1] = cnt
        else:
            counter[maxnum] = cnt - n
            if maxnum - 1 in counter:
                counter[maxnum-1] += n
            else:
                counter[maxnum-1] = n
            n = 0
            
    result = 0
    for c in counter.items():
        cnum, ccnt = c
        for i in range(ccnt):
            result += cnum ** 2
                
    return result