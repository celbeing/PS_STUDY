import sys
input = sys.stdin.readline
N,M = map(int,input().split())
tkh = [[] for _ in range(N+1)]
cnt = [0]*(N+1)
for _ in range(M):
    t,p = map(int,input().split())
    tkh[p].append(t)
    cnt[p] += 1
for _ in range(int(input())):
    A,B = map(int,input().split())
    res = 0
    a,b = 0,0
    while a < cnt[A] and b < cnt[B]:
        if tkh[A][a] <= tkh[B][b] < tkh[A][a+1]:
            if tkh[A][a+1] >= tkh[B][b+1]:
                res += tkh[B][b+1]-tkh[B][b]
                b += 2
            else:
                res += tkh[A][a+1]-tkh[B][b]
                a += 2
        elif tkh[B][b] < tkh[A][a] < tkh[B][b+1]:
            if tkh[B][b+1] >= tkh[A][a+1]:
                res += tkh[A][a+1]-tkh[A][a]
                a += 2
            else:
                res += tkh[B][b+1]-tkh[A][a]
                b += 2
        elif tkh[A][a] >= tkh[B][b+1]: b += 2
        else: a += 2
    print(res)