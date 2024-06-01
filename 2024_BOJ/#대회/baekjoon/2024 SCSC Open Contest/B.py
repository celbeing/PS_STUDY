import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
infested = list(map(int,input().split()))
log = [tuple(map(int,input().split())) for _ in range(M)]
log.sort()
for i in range(1,N+1):
    sum = 1
    infest = [False]*(N+1)
    infest[i] = True
    for t,a,b in log:
        if infest[a] and not infest[b]:
            infest[b] = True
            sum += 1
    flag = True
    if sum != K: continue
    for k in infested:
        if infest[k]:
            continue
        else:
            flag = False
            break
    if flag:
        print(i)
        break