import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def toPost(p_s, p_e, i_s, i_e):
    global postorder
    
    if p_s <= p_e and i_s <= i_e:
        root = preorder[p_s]
        idx = inorder.index(root)
        
        toPost(p_s + 1, p_s + idx - i_s, i_s, idx - 1 )
        toPost(p_s + idx - i_s + 1, p_e, idx + 1, i_e)
        postorder.append(root)
    
    else:
        return
    
for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = []
    toPost(0, n-1, 0, n-1)
    
    print(*postorder)