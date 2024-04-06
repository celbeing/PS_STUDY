#B: 조용히 하라고!!
import sys
input = sys.stdin.readline
N,M,K,T,P = map(int,input().split())
mogi = [list(map(int,input().split())) for _ in range(K)]

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def woojeong(route,depth,record,t):
    if record < depth: record = depth
    if depth == K: return record
    for i in range(K):
        if i in route: continue
        d = dist((mogi[route[-1]][0],mogi[route[-1]][1]),(mogi[i][0],mogi[i][1]))
        if t+d > T: continue
        route.append(i)
        record = woojeong(route,depth+1,record,t+d)
        route.pop()
    return record
def areum(P,N,M,mogi):
    killed = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for m in mogi:
                d = dist((m[0], m[1]), (i, j))
                if m[2] * d <= P:
                    count += 1
            if count > killed:
                killed = count
    return killed

wj = 1
for i in range(K):
    k = woojeong([i],1,1,0)
    if wj < k: wj = k
ar = areum(P,N,M,mogi)

print(wj,ar)