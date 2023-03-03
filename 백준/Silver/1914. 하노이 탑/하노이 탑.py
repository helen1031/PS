n = int(input())
moves = []

def hanoi(i, start, mid, goal):
    if i == 1:
        print(start, goal)
        return
    
    # n-1개를 start에서 mid로 옮긴다
    hanoi(i-1, start, goal, mid)
    
    # n을 start에서 goal로 옮긴다
    print(start, goal)
    
    # n-1개를 mid에서 goal로 옮긴다
    hanoi(i-1, mid, start, goal)

print(2**n - 1) # hanoi 함수를 2번씩 호출하므로
if n <= 20:
    hanoi(n, 1, 2, 3)