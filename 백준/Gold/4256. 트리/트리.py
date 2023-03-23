import sys
input = sys.stdin.readline

def toPost(p_s, p_e, i_s, i_e):

    if p_s <= p_e and i_s <= i_e:
        root = preorder[p_s]
        ridx = inorder.index(root)

        # 왼쪽
        toPost(p_s + 1, p_s + ridx - i_s, i_s, ridx - 1)
        # 오른쪽
        toPost(p_s + ridx - i_s + 1, p_e, ridx + 1, i_e)
        # 루트
        postorder.append(root)

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = []

    toPost(0, n-1, 0, n-1)

    print(*postorder)