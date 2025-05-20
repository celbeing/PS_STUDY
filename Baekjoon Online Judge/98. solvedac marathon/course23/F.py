#6213: Balanced Lineup
import sys
input = sys.stdin.readline

def seg_init(tree, node, s, e, array):
    if s == e:
        tree[node] = (array[s], array[s])
    else:
        m = (s + e) // 2
        l = node * 2
        r = l + 1
        seg_init(tree, l, s, m, array)
        seg_init(tree, r, m + 1, e, array)

        mn = min(tree[l][0], tree[r][0])
        mx = max(tree[l][1], tree[r][1])
        tree[node] = (mn, mx)

def seg_get(tree, node, s, e, l, r):
    mn, mx = 1000000, 0
    if l > e or r < s: return (1000000, 0)
    elif l <= s and e <= r: return tree[node]
    m = (s + e) // 2
    lmn, lmx = seg_get(tree, node * 2, s, m, l, r)
    rmn, rmx = seg_get(tree, node * 2 + 1, m + 1, e, l, r)
    return (min(lmn, rmn), max(lmx, rmx))

def solution():
    N, Q = map(int, input().split())
    cow = [0] + [int(input()) for _ in range(N)]
    seg_h = 0
    while 1 << seg_h < N:
        seg_h += 1
    seg_h += 1
    seg = [(1000000, 0)] * (1 << seg_h)
    seg_init(seg, 1, 1, N, cow)
    for _ in range(Q):
        A, B = map(int, input().split())
        mn, mx = seg_get(seg, 1, 1, N, A, B)
        print(mx - mn)
solution()