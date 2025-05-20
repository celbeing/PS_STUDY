import sys
input = sys.stdin.readline
N = int(input())
d = [(1,0),(0,1),(0,-1),(-1,0)]

bt = [(0,0),(-1,0),(-1,1)]
count = 0

def backtracking(depth):
    global count
    x,y = bt[-1]
    k = 1
    if (x+y)&1: k = 0
    if depth == N:
        for i in range(k, k+3):
            dx = x+d[i][0]
            dy = y+d[i][1]
            for j in range(N-3):
                if bt[j] == (dx,dy):
                    count += 1
                    break
        return
    for i in range(k, k+3):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if (dx,dy) in bt: continue
        bt.append((dx,dy))
        backtracking(depth+1)
        bt.pop()
    return

if N > 1: backtracking(2)
print(count*2)
"""
N = [0,0,0,0,0,2,2,4,8,26,36,80,148,332,556,1172,2112,4350,7732,15568,28204,56100,101640]
print(N[int(input())])
"""