# 15678: 연세워터파크
import sys
from math import ceil, log2
input = sys.stdin.readline

n, d = map(int, input().split())
k = list(map(int, input().split()))

h = 2 << ceil(log2(n))
seg_tree = [-int(1e9+1)] * h
dp = [-int(1e9)] * n
result = -int(1e9)

def init(s, e, node):
    if s == e:
        seg_tree[node] = k[s]
        return
    else:
        m = (s + e) // 2
        l = node << 1
        r = l + 1
        init(s, m, l)
        init(m + 1, e, r)
        if seg_tree[l] < seg_tree[r]:
            seg_tree[node] = seg_tree[r]
        else:
            seg_tree[node] = seg_tree[l]
        return

def query(s, e, l, r, node):
    if l > e or r < s:
        return -int(1e9 + 1)

    if l <= s and e <= r:
        return seg_tree[node]

    m = (s + e) // 2
    lq = query(s, m, l, r, node << 1)
    rq = query(m + 1, e, l, r, (node << 1) + 1)
    return max(lq, rq)

def modify(s, e, node, target, p):
    while s < e:
        m = (s + e) // 2
        node <<= 1
        if m < target:
            s = m + 1
            node += 1
        else:
            e = m
    while node:
        if seg_tree[node] < p:
            seg_tree[node] = p
            node >>= 1
        else:
            break
    return

init(0, n - 1, 1)

for i in range(d + 1):
    maximum = query(0, n - 1, 0, i - 1, 1) + k[i]
    modify(0, n - 1, 1, i, maximum)

for i in range(d, n):
    maximum = query(0, n - 1, i - d, i - 1, 1) + k[i]
    modify(0, n - 1, 1, i, maximum)

print(seg_tree[1])
