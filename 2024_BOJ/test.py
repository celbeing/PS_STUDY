import sys
input = sys.stdin.readline

s, d, i, l, N = map(int, input().split())
e = s + d + i + l
if e >= N*4: print(0)
else: print(N*4-e)