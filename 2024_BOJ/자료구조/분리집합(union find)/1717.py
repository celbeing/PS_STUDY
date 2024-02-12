#1717: 집합의 표현
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
union = [i for i in range(n+1)]

def head(k):
    while union[k] != k:
        k = union[k]
    return k

for _ in range(m):
    s,a,b = map(int,input().split())
    if s == 0:
        if a == b: continue
        A = head(a)
        B = head(b)
        union[B] = A
    else:
        A = head(a)
        B = head(b)
        union[a] = A
        union[b] = B
        if A == B:
            print("YES")
        else:
            print("NO")