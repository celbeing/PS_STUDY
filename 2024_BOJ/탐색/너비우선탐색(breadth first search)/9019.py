#9019: DSLR
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    path = ['' for _ in range(10001)]
    A, B = map(int,input().split())
    path[A] = ''
    bfs = deque([A])
    while bfs:
        now = bfs.popleft()
        if now == B:
            print(path[now])
            break

        d = (now*2)%10000
        s = (now+9999)%10000
        l = (now*10+now//1000)%10000
        r = (now//10)+(now%10)*1000

        if not path[d] and d != A:
            path[d] = path[now] + 'D'
            bfs.append(d)
        if not path[s] and s != A:
            path[s] = path[now] + 'S'
            bfs.append(s)
        if not path[l] and l != A:
            path[l] = path[now] + 'L'
            bfs.append(l)
        if not path[r] and r != A:
            path[r] = path[now] + 'R'
            bfs.append(r)