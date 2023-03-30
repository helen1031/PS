import sys
input = sys.stdin.readline

import heapq

n = int(input())
lectures = []
for _ in range(n):
    no, start, end = map(int, input().split())
    lectures.append((no, start, end))
lectures.sort(key=lambda x: (x[1], x[2], x[0]))

cnt = 1
cno, cstart, cend = lectures[0]

classrooms = []    # heapq
heapq.heappush(classrooms, (cend, 1))

cinfo = [0] * (n + 1)
cinfo[cno] = 1

for i, lecture in enumerate(lectures[1:]):
    no, start, end = lecture
    classend, classno = classrooms[0] # 가장 빨리 끝나는 강의
    if classend <= start:
        heapq.heappop(classrooms)
        heapq.heappush(classrooms, (end, classno))
        cinfo[no] = classno
    else:
        cnt += 1
        heapq.heappush(classrooms, (end, cnt))
        cinfo[no] = cnt

print(cnt)
for c in cinfo[1:]:
    print(c)