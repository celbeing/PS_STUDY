# 19687: Experimental Charges
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, q = map(int, input().split())
    p = [[i, 0] for i in range(n + 1)]
    def find(k):
        if k == p[k][0]:
            return (k, 0)
        head, par = find(p[k][0])
        p[k][0] = head
        p[k][1] ^= par
        return (p[k][0], p[k][1])

    def union(a, b, s):
        A, Apar = find(a)
        B, Bpar = find(b)
        if A == B: return
        elif A < B:
            p[A][0] = B
            p[A][1] = Apar ^ Bpar ^ s
        else:
            p[B][0] = A
            p[B][1] ^= Apar ^ Bpar ^ s
        return

    for _ in range(q):
        Q, a, b = map(str, input().split())
        a, b = int(a), int(b)
        if Q == 'Q':
            A, Apar = find(a)
            B, Bpar = find(b)
            if A == B:
                print('R' if Apar == Bpar else 'A')
            else:
                print('?')
        else:
            union(a, b, 1 if Q == 'A' else 0)
solution()