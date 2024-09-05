import sys
input = sys.stdin.readline

def sol():
    N, K = map(int, input().split())
    bucket = [tuple(map(int, input().split())) for _ in range(N)]
    bucket.sort(key = lambda x: x[1])
    ice = 0
    l, r = 0, 0
    for g, x in bucket:
        if x > K: break
        r += 1
        ice += g
    res = ice
    for albert in range(1000000):
        if r == N: break
        if bucket[l][1] < albert - K:
            ice -= bucket[l][0]
            l += 1
        if bucket[r][1] <= albert + K:
            ice += bucket[r][0]
            r += 1
            if res < ice: res = ice
    print(res)
sol()