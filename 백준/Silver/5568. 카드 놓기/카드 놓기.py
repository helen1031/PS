n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
used = [False for _ in range(n)]
select = []
choices = []

def rec(idx):
    if len(select) == k:
        choices.append(''.join(select))
        return
    for i in range(n):
        if used[i]:
            continue
        select.append(cards[i])
        used[i] = True
        rec(i+1)
        select.pop()
        used[i] = False
        
    
rec(0)
print(len(set(choices)))