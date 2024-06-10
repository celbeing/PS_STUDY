import sys
input = sys.stdin.readline
mod = 998244353
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    large = abs(a[0])
    small = a[0]
    caseL,caseS = 0,0
    if a[0] >= 0: caseL,caseS = 2,0
    else: caseL,caseS = 1,1
    for i in range(1,n):
        l,s = 0,0
        cl,cs = 0,0
        if a[i] == 0:
            caseL *= 2
            caseL %= mod
            if small >= 0:
                caseS *= 2
                caseS %= mod
            continue
        elif a[i] > 0:
            l = large+a[i]
            caseL *= 2
            caseL %= mod
            s = small+a[i]
        else:
            l = max(large+a[i],abs(small+a[i]))
            s = small+a[i]
        large = l
        small = s
    print(max(large,abs(small)))