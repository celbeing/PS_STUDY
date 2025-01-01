# 32203: 연락
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    c = [-1] + list(map(int, input().split()))
    head = [i for i in range(n + 1)]
    count = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if c[i] & 1:
            count[i][0] += 1
        else:
            count[i][1] += 1
    def find(k):
        while head[k] != k:
            k = head[k]
        return k
    def union(a, b):
        A = find(a)
        B = find(b)
        ret = 0
        ret -= count[A][0] * count[A][1]
        ret -= count[B][0] * count[B][1]
        if A > B:
            head[B] = a
            count[A][0] += count[B][0]
            count[A][1] += count[B][1]
            ret += count[A][0] * count[A][1]
        else:
            head[A] = b
            count[B][0] += count[A][0]
            count[B][1] += count[A][1]
            ret += count[B][0] * count[B][1]
        return ret
    res = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b):
            res += union(a, b)
        print(res)
solution()