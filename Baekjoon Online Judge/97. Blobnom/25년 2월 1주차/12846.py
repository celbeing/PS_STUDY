# 12846: 무서운 아르바이트
import sys
from math import ceil, log2
input = sys.stdin.readline
def solution():
    n = int(input())
    t = list(map(int, input().split()))
    seg_tree = [0] * (1 << (ceil(log2(n)) + 1))

    def init(node, s, e):
        if s == e:
            seg_tree[node] = s
        else:
            m = (s + e) // 2
            l = node << 1
            r = l + 1
            init(l, s, m)
            init(r, m + 1, e)
            if t[seg_tree[l]] < t[seg_tree[r]]:
                seg_tree[node] = seg_tree[l]
            else:
                seg_tree[node] = seg_tree[r]

    init(1, 0, n - 1)

    def query(node, s, e, l, r):
        if l > e or r < s:
            return -1
        if l <= s and e <= r:
            return seg_tree[node]

        m = (s + e) // 2
        next = node << 1
        left = query(next, s, m, l, r)
        right = query(next + 1, m + 1, e, l, r)

        if left == -1:
            return right
        elif right == -1:
            return left
        elif t[left] < t[right]:
            return left
        else:
            return right

    def div_conq(l, r):
        if l > r:
            return 0
        if l == r:
            return t[l]

        ret = 0
        div = query(1, 0, n - 1, l, r)
        ret = (r - l + 1) * t[div]
        left = div_conq(l, div - 1)
        right = div_conq(div + 1, r)
        if ret < left:
            ret = left
        if ret < right:
            ret = right
        return ret

    print(div_conq(0, n - 1))
solution()