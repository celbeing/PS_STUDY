#1640: 동전 뒤집기
import sys
input = sys.stdin.readline
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
if h_odd&1:
    res = min(h_odd+M-v_odd,v_odd+N-h_odd)
else:
    if h_odd == 0 or v_odd == 0:
        res = max(v_odd,h_odd)
    elif h_odd+v_odd:
        res = N+M-h_odd-v_odd
print(res)