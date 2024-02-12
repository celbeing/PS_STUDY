#1389: 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
inf = 1e9
N,M = map(int,input().split())
friend = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
kevin = [[inf for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    kevin[i][i] = 0
    for j in friend[i]:
        kevin[i][j] = 1
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            kevin[i][j] = min(kevin[i][j],kevin[i][k]+kevin[k][j])
bacon = [0]*(N+1)
minimum = inf
answer = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        bacon[i] += kevin[i][j]
    if bacon[i] < minimum:
        minimum = bacon[i]
        answer = i
print(answer)