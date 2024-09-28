# 28107: 회전초밥
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
susi = [[] for _ in range(200001)]
ate = [0]*N
pick = [0]*200001
for n in range(N):
    o = list(map(int,input().split()))
    for i in range(1,o[0]+1):
        susi[o[i]].append(n+1)
b = list(map(int,input().split()))
for s in b:
    if len(susi[s]) == pick[s]: continue
    ate[susi[s][pick[s]]-1] += 1
    pick[s] += 1
print(*ate)