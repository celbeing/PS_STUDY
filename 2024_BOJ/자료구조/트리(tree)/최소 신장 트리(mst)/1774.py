#1774: 우주신과의 교감
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

root = [i for i in range(N+1)]
def find(k,r):
    while k != r[k]: k = r[k]
    return k

dist = []
gods = []
for i in range(1,N+1):
    x,y = map(int,input().split())
    for j in range(1,i):
        dist.append(((x-gods[j-1][0])**2+(y-gods[j-1][1])**2,i,j))
    gods.append([x,y])
dist.sort(reverse=True)

count = 0
result = 0

for _ in range(M):
    a,b = map(int,input().split())
    root_a = find(a,root)
    root_b = find(b,root)
    if root_a == root_b: continue
    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b
    count += 1

while dist and count < N-1:
    d,a,b = dist.pop()
    root_a = find(a,root)
    root_b = find(b,root)
    if root_a == root_b: continue
    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b
    count += 1
    result += d**0.5

print("{:.2f}".format(round(result,2)))