import sys
input = sys.stdin.readline
E,EM,M,MH,H = map(int,input().split())

def check(k):
    dif = [E,EM,M,MH,H]
    e,m,h = k,k,k
    if e > dif[0]:
        e -= dif[0]
        if e > dif[1]: return False
        else: dif[1] -= e

    if m > dif[1]:
        m -= dif[1]
        if m > dif[2]:
            m -= dif[2]
            if m > dif[3]: return False
            else: dif[3] -= m

    if h > dif[3]:
        h -= dif[3]
        if h > dif[4]: return False

    return True

s,e = 0,170000
while s<e:
    m = (s+e)//2
    if check(m):
        s = m+1
    else:
        e = m

if check(s):
    while check(s):
        s += 1
    print(s-1)
else:
    while not(check(s)):
        s -= 1
    print(s)