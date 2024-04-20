#2653: 안정된 집단
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
group = []
check = [0]*n

for i in range(n):
    if check[i]: continue
    f = [i]
    check[i] = 1
    for j in range(n):
        if i == j: continue
        if graph[i][j] == 0:
            f.append(j)
            check[j] = 1
    if len(f) == 1:
        print(0)
        exit()
    for j in f:
        for k in range(n):
            if j == k: continue
            if graph[j][k] == 0:
                if not(k in f):
                    print(0)
                    exit()
    group.append(f)
print(len(group))
for i in group:
    for j in range(len(i)):
        i[j] += 1
    print(*i)