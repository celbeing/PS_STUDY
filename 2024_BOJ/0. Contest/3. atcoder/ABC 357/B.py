import sys
input = sys.stdin.readline
S = list(input().rstrip())
u,d = 0,0
for s in S:
    if s.isupper(): u += 1
    else: d += 1
if u > d:
    print("".join(S).upper())
else:
    print("".join(S).lower())