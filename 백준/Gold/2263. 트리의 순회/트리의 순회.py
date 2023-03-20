import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

def find(ins, ine, pos, poe):
    if ins <= ine and pos <= poe:
        root = postorder[poe]
        preorder.append(root)
        idx = inorder.index(root)
        find(ins, idx-1, pos, pos + idx - ins -1)
        find(idx + 1, ine, pos + idx - ins, poe - 1)
    else:
        return
    
find(0, n-1, 0, n-1)

print(*preorder)