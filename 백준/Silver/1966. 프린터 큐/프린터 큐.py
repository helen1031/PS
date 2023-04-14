import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))

    documents = deque([])
    for i, d in enumerate(doc):
        documents.append((i, d))

    doc.sort()
    maxcost = doc[-1]
    cnt = 1
    while documents:
        idx, cost = documents[0]
        if cost != maxcost:
            documents.append(documents.popleft())
        else:
            if idx == m:
                print(cnt)
                break
            else:
                documents.popleft()
                cnt += 1
                doc.pop()
                maxcost = doc[-1]