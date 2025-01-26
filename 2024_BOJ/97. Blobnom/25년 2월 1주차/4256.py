# 4256: 트리
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n = int(input())
        pr_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        def pt_order(p, i):
            if p:
                root = p[0]
                k = i.index(root)
                l_sub = pt_order(p[1:k + 1], i[:k])
                r_sub = pt_order(p[k + 1:], i[k + 1:])
                return l_sub + r_sub + [root]
            else:
                return []

        print(*pt_order(pr_order, in_order))
solution()