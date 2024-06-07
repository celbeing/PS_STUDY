#9870: Vaction Planning
import sys
input = sys.stdin.readline
N,M,K,Q = map(int,input().split())
inf = 1e9
floyd = [[inf for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    u,v,d = map(int,input().split())
    floyd[u][v] = d

for i in range(1, N+1):
    floyd[i][i] = 0
    for j in range(1, N+1):
        for k in range(1, N+1):
            new_d = floyd[j][i] + floyd[i][k]
            if floyd[j][k] > new_d:
                floyd[j][k] = new_d

route = 0
cost = 0

for _ in range(Q):
    a,b = map(int,input().split())
    least = inf
    for i in range(1, K+1):
        new_d = floyd[a][i] + floyd[i][b]
        if least > new_d:
            least = new_d
    if least < inf:
        route += 1
        cost += least

print(route)
print(cost)