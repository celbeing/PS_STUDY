#E: blob_twintail_thinking
import sys
from collections import deque
input = sys.stdin.readline
D,N,U,T = map(int,input().split())
limit = 2**D-1
block = dict()
for _ in range(N):
    s,e = map(int,input().split())
    if s in block:
        block[s].append(e)
    else:
        block[s] = [e]
last = 0
twin = deque([(1,U)])
dist_twin = 0
while twin:
    now,dist = twin.popleft()
    last = now
    l = now*2
    r = l+1
    if l > limit:
        continue
    if now in block:
        if l in block[now]:
            pass
        else:
            dist_twin += dist
            twin.append((l,dist+T))
        if r in block[now]:
            pass
        else:
            dist_twin += dist
            twin.append((r,dist+T))

def pony(now,dist):
    if now == last:
        if dist > dist_twin:
            print(":blob_twintail_aww:")
        elif dist < dist_twin:
            print(":blob_twintail_sad:")
        else:
            print(":blob_twintail_thinking:")
        exit()

    l = now * 2
    r = l + 1
    if l > limit:
        return dist
    if now in block:
        if l in block[now]:
            pass
        else:
            dist += U
            dist = pony(l,dist)
        if r in block[now]:
            pass
        else:
            dist += U
            dist = pony(r,dist)
    return dist + U

pony(1,0)