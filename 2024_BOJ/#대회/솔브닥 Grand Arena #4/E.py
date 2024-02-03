#E번 - 트리 탐색기
import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
folder = [[0,0,0] for _ in range(N+1)]
origin = [[] for _ in range(N+1)]
for i in range(1,N+1):
    lower = list(map(int,input().split()))
    origin[i] = lower[1:]
    if lower[0] == 0: continue
    folder[lower[1]][1] = i
    folder[lower[1]][0] = i
    for j in range(lower[0]-1):
        folder[lower[j+1]][0] = i
        folder[lower[j+1]][2] = lower[j+2]
        folder[lower[j+2]][1] = lower[j+1]
    folder[lower[-1]][2] = folder[i][2]
    folder[lower[-1]][0] = i

cursor = 2
for i in range(Q):
    order = list(input().split())
    if order[0] == "move":
        k = int(order[1])
        while k > 0:
            t = folder[cursor][2]
            if t > 1:
                cursor = t
                k -= 1
            else:
                break
        while k < 0:
            t = folder[cursor][1]
            if t > 1:
                cursor = t
                k += 1
            else:
                break
        print(cursor)
    else:
        if origin[cursor]:
            if folder[cursor][2] == origin[cursor][0]:
                t = cursor
                while folder[t][0]
            else:
                folder[cursor][2] = origin[cursor][0]