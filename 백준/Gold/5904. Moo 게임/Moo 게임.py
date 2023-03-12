n = int(input())
k = 0
length = 3
info = [length]

def moo(nn, kk):
    if kk == 0:
        if nn == 1:
            return "m"
        else:
            return "o"
    kk -= 1
    if nn <= info[kk]:
        return moo(nn, kk)
    elif nn == info[kk] + 1:
        return "m"
    elif info[kk] + 1 < nn <= info[kk] + 1 + kk + 2:
        return "o"
    else:
        return moo(nn - info[kk] - 1 - kk - 3, kk)
    
while length < n:
    k += 1
    length = length * 2 + k + 3
    info.append(length)

ans = moo(n, k)
print(ans)