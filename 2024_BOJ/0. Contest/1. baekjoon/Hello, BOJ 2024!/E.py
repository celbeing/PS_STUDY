#E: 신제품 개발
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
graph = dict()
for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    u,v,B = map(int,input().split())
    graph[u].append((B,v))
for i in range(1, N+1):
    graph[i].sort(reverse=True)

u,c = 1,0

k = 1
while k <= K:
    B, v = 0,0
    for b, V in graph[u]:
        B = b
        v = V
        if b <= c:
            break
    if v > 0:
        k += 1
        u = v
        c += A[u]
    else:
        gap = B - c
        if gap % A[u] == 0:
            k += gap//A[u]
            u = v
            c = B
        else:
            k += gap//A[u] + 1
            c += (gap//A[u] + 1)*A[u]

            if k > K:
                c -= (K-k)*A[u]
                print(u,c%1000000007)
                exit()
            else:
                u = v
print(u,c%1000000007)