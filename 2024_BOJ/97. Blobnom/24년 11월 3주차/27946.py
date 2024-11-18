# 27945: 슬슬 가지를 먹지 않으면 죽는다
import sys
input = sys.stdin.readline
def solution:
    n, m = map(int, input().split())
    link = [tuple(map(int, input().split())) for _ in range(m)]
    link.sort(key = lambda: x[2])
    head = [i for i in range(n + 1)]
    
    def union(a, b):
        A = find(a)
        B = find(b)
        if A <= B:
            pass
        else:
            pass
        return 0

    def find(k):
        while head[k] != k:
            k = head[k]
        return k
    k = 1
    