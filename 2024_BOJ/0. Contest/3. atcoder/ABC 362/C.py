import sys
input = sys.stdin.readline

N = int(input())
LC, RC = 0,0
pre = []
for _ in range(N):
    L,R = map(int,input().split())
    LC += L
    RC += R
    pre.append((LC,RC))
if LC<=0<=RC:
    print("Yes")

else:
    print("No")