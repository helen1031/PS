for _ in range(int(input())):
    tot = 0
    s = input()
    
    cnt = 0
    for c in s:
        if c == 'O':
            cnt += 1
        else:
            cnt = 0
        tot += cnt
    print(tot)