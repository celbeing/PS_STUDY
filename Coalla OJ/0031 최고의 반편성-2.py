import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    count = [0] * n
    m = sum(list(map(int, input().split())))
    f = []
    for i in range(n):
        score = list(map(int, input().split()))
        for s in score:
            f.append((s, i))
    f.sort()
    s, e = 0, -1
    find = 0
    while find < n:
        e += 1
        if count[f[e][1]] == 0: find += 1
        count[f[e][1]] += 1
    res = f[e][0] - f[s][0]
    while e < m:
        if count[f[s][1]] == 1:
            e += 1
            while e < m and f[e][1] != f[s][1]:
                count[f[e][1]] += 1
                e += 1
            if e == m: break
        else:
            count[f[s][1]] -= 1
        s += 1
        res = min(res, f[e][0] - f[s][0])
    print(res)
solution()