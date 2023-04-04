from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    possible = True
    while goal:
        current = goal.popleft()
        if cards1 and cards1[0] == current:
            cards1.popleft()
        elif cards2 and cards2[0] == current:
            cards2.popleft()
        else:
            possible = False
            break
            
    if possible:
        return "Yes"
    else:
        return "No"