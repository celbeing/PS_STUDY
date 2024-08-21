#17488: 수강바구니
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L = list(map(int,input().split()))
count = [0]*M
res = [[] for _ in range(N)]
S = [[] for _ in range(M)]
for i in range(N):
    apply = list(map(int,input().split()))[:-1]
    for a in apply:
        S[a-1].append(i)
for i in range(M):
    if len(S[i]) > L[i]: continue
    else:
        for s in S[i]:
            res[s].append(i+1)
        L[i] -= len(S[i])
        S[i].clear()
for i in range(N):
    apply = list(map(int,input().split()))[:-1]
    for a in apply:
        S[a-1].append(i)
for i in range(M):
    if len(S[i]) > L[i]: continue
    else:
        for s in S[i]:
            res[s].append(i+1)
        L[i] -= len(S[i])
        S[i].clear()
for i in range(N):
    if len(res[i])>0:
        print(*sorted(res[i]))
    else:
        print("망했어요")