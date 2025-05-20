#1640: 동전 뒤집기
import sys
input = sys.stdin.readline
<<<<<<< Updated upstream
def solution():
    N, M = map(int, input().split())
    v = [0] * M
    h = [0] * N
    for i in range(N):
        row = list(input().strip())
        for j in range(M):
            if row[j] == "1":
                v[j] = 0 if v[j] else 1
                h[i] = 0 if h[i] else 1

    v = sum(v)
    h = sum(h)

    res = 0
    if N & 1 and M & 1:
        if v & 1 and h & 1:
            res = min(v + N - h, h + M - v)
        else:
            res = min(v, h)
    elif N & 1:

    print(res)
solution()
=======
N,M = map(int,input().split())
coin = [list(input().rstrip()) for _ in range(N)]
vert,hori = [0]*M,[0]*N
for i in range(N):
    for j in range(M):
        if coin[i][j] == "1":
            hori[i] = 0 if hori[i] else 1
            vert[j] = 0 if vert[j] else 1
h_odd,v_odd = 0,0
for i in range(N):
    if hori[i]: h_odd += 1
for i in range(M):
    if vert[i]: v_odd += 1
res = 0
if h_odd & 1 and v_odd & 1:
    res = min(h_odd+M-v_odd,v_odd+N-h_odd)
else:
    if h_odd == 0 or v_odd == 0:
        res = max(v_odd,h_odd)
    elif h_odd+v_odd:
        res = N+M-h_odd-v_odd
    else:
        res = -1
print(res)
>>>>>>> Stashed changes
