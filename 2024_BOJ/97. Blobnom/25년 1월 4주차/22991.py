# 22991: 수요응답형 버스
import sys
from math import ceil, log2
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    b = [tuple(map(int, input().split())) for _ in range(m)]

    time = set()
    counter = dict()
    for c, t in p:
        time.add(t)
        counter[t] = 0
    keys = sorted(list(time))
    leaf = dict()
    seg_tree = [0] * (1 << (ceil(log2(len(keys)))+1))

    p.sort()
    b.sort()

    def init(l, r, node):
        if l == r:
            leaf[keys[l]] = node
            return
        m = (l + r) >> 2
        init(l, m, node << 1)
        init(m + 1, r, (node << 1) + 1)
        return

    def add(k):
        counter[k] += 1
        node = leaf[k]
        while node:
            if seg_tree[node] < k:
                seg_tree[node] = k
                node >>= 1
            else: break
        return

    def dele(k):
        counter[k] -= 1
        if counter[k] == 0:
            node = leaf[k]
            seg_tree[node] = 0
            node >>=  1
            while node:
                if seg_tree[node] == seg_tree[node * 2 + 1]: return
                elif seg_tree[node * 2 + 1]: seg_tree[node] = seg_tree[node * 2 + 1]
                else: seg_tree[node] = seg_tree[node << 1]
                node >>= 1
        return

    def find(k):
        node = 1
        s, e = 0, len(keys) - 1
        while s < e:
            m = (s + e) // 2
            node <<= 1
            if k <= seg_tree[node]:
                e = m
            elif k <= seg_tree[node + 1]:
                s = m + 1
                node += 1
            else:
                return -1
        if k <= seg_tree[node]:
            return keys[s]
        else:
            return -1

    init(0, len(keys) - 1, 1)

    i = 0
    count = 0
    for c, t in b:
        while i < n and p[i][0] <= c:
            add(p[i][1])
            i += 1
        k = find(t)
        if k > 0:
            count += 1
            dele(k)

    print(count)
solution()