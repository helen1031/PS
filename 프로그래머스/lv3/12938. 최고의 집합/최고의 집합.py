def solution(n, s):
    if n > s : 
        return [-1]
    
    num = s // n
    last = s - num * n
    
    answer = [num] * n
    
    idx = -1
    while last != 0:
        answer[idx] += 1
        last -= 1
        idx -= 1 
    return answer