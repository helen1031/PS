e, s, m = map(int, input().split())

def find(eidx, sidx, midx):
    te = e + 15 * eidx
    ts = s + 28 * sidx
    tm = m + 19 * midx
    if te == ts and ts == tm and tm == te:
        print(te)
        return
    mt = max(te, ts, tm)
    if te < mt:
        eidx += 1
    if ts < mt:
        sidx += 1
    if tm < mt:
        midx += 1
    find(eidx, sidx, midx)
    
find(0, 0, 0)