n = int(input())
print(2 ** n -1)
def hanoi(cnt, start, goal, sub):
    if cnt == 1:
        print(start, goal)
        return
    hanoi(cnt - 1, start, sub, goal)
    print(start, goal)
    hanoi(cnt - 1, sub, goal, start)
    
hanoi(n, 1, 3, 2)