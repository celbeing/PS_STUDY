#6497: 전력난
import sys
input = sys.stdin.readline

def find(k,r):
    while k != r[k]: k = r[k]
    return k

while True:
    m,n = map(int,input().split())
    if m+n == 0: break
    root = [i for i in range(m+1)]
    road = [tuple(map(int,input().split())) for _ in range(n)]
    road.sort(reverse=True, key = lambda x: x[2])

    counter = 0
    saved = 0
    while road and counter < m-1:
        a,b,r = road.pop()
        root_a = find(a,root)
        root_b = find(b,root)
        if root_a == root_b:
            saved += r
            continue
        if root_a < root_b:
            root[root_b] = root_a
        else:
            root[root_a] = root_b
        counter += 1
    while road:
        a,b,r = road.pop()
        saved += r
    print(saved)