#4195: 친구 네트워크
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
T = int(input())

def head(k):
    while friend[k] != k:
        k = friend[k]
    return k

def union(a, b):
    A = head(a)
    friend[a] = A
    B = head(b)
    friend[b] = B
    if A != B:
        friend[B] = A
        size[A] += size[B]
    print(size[A])

for _ in range(T):
    F = int(input())
    friend = {}
    size = {}
    for _ in range(F):
        a, b = input().split()
        if a not in friend:
            friend[a] = a
            size[a] = 1
        if b not in friend:
            friend[b] = b
            size[b] = 1
        union(a, b)