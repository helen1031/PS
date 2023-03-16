import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
        
def postorder(start, end):
    if start > end :
        return 
    root = tree[start]
    mid = end + 1
    for i in range(start + 1, end + 1):
        if root < tree[i]:
            mid = i
            break
    postorder(start + 1, mid-1)
    postorder(mid, end)
    print(root)
    
postorder(0, len(tree) - 1)