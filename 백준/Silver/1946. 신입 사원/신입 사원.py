import sys
for _ in range(int(input())):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    applicants.sort()
    target = applicants[0][1]
    cnt = 1
    for applicant in applicants[1:]:
        if applicant[1] <= target:
            cnt += 1
            target = applicant[1]
    print(cnt)
            