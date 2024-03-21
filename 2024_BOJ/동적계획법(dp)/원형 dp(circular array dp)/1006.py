#1006: 습격자 초라기
import sys
input = sys.stdin.readline

def solve(k):
    for i in range(k,N):
        a[i+1] = min(b[i]+1,c[i]+1)
        if o[0][i]+o[1][i] <= W:
            a[i+1] = min(a[i+1],a[i]+1)
        if i > 0 and o[0][i-1]+o[0][i] <= W and o[1][i-1]+o[1][i] <= W:
            a[i+1] = min(a[i+1],a[i-1]+2)
        if i < N-1:
            b[i+1] = a[i+1]+1
            if o[0][i]+o[0][i+1] <= W:
                b[i+1] = min(b[i+1],c[i]+1)
            c[i+1] = a[i+1]+1
            if o[1][i]+o[1][i+1] <= W:
                c[i+1] = min(c[i+1],b[i]+1)

T = int(input())
for _ in range(T):
    N,W = map(int,input().split())
    o = [list(map(int,input().split())) for _ in range(2)]
    a = [0] * (N+1)
    b = [0] * N
    c = [0] * N
    b[0] = 1
    c[0] = 1
    solve(0)
    result = a[N]

    if N > 1 and o[0][0]+o[0][N-1] <= W:
        a[1] = 1
        b[1] = 2
        if o[1][0]+o[1][1] <= W:
            c[1] = 1
        else:
            c[1] = 2
        solve(1)
        result = min(result,c[N-1]+1)

    if N > 1 and o[1][0]+o[1][N-1] <= W:
        a[1] = 1
        if o[0][0]+o[0][1] <= W:
            b[1] = 1
        else:
            b[1] = 2
        c[1] = 2
        solve(1)
        result = min(result,b[N-1]+1)

    if N > 1 and o[0][0]+o[0][N-1] <= W and o[1][0]+o[1][N-1] <= W:
        a[1] = 0
        b[1] = 1
        c[1] = 1
        solve(1)
        result = min(result,a[N-1]+2)

    print(result)