import sys
sys.setrecursionlimit(10**6)

answer = 0

def solution(numbers, target):
    
    def dfs(idx, total):
        global answer
        
        if idx == len(numbers) -1 and total == target:
            answer += 1
            return
        
        if idx + 1 <= len(numbers) - 1:
            dfs(idx+1, total + numbers[idx+1])
            dfs(idx+1, total - numbers[idx+1])
        
    dfs(0, numbers[0])
    dfs(0, -numbers[0])
    
    return answer