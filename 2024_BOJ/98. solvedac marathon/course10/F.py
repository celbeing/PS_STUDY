#2187: 점 고르기
import sys
input = sys.stdin.readline
N,A,B = map(int,input().split())
dots = []
res = 0
for _ in range(N):
    r,c,s = map(int,input().split())
    for dr,dc,ds in dots:
        if abs(r-dr) < A and abs(c-dc) < B and res < abs(s-ds):
            res = abs(s-ds)
    dots.append((r,c,s))
print(res)