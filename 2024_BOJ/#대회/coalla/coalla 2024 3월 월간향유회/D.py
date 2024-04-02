#11286: 절댓값 힙
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())
hp = []
hm = []
cp,cm = 0,0
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(hp,x)
        cp += 1
    elif x < 0:
        heappush(hm,-x)
        cm += 1
    else:
        if cp+cm == 0:
            print(0)
        elif cp == 0:
            print(-heappop(hm))
            cm -= 1
        elif cm == 0:
            print(heappop(hp))
            cp -= 1
        else:
            if hp[0] < hm[0]:
                print(heappop(hp))
                cp -= 1
            else:
                print(-heappop(hm))
                cm -= 1