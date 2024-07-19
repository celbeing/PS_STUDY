import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ss = list(map(int,input().split()))
es = list(map(int,input().split()))
c1 = []
c2 = []

for i in range(M):
    if i&1:
        c1 += [0]*es[i]
        c2 += [1]*es[i]
    else:
        c1 += [1]*es[i]
        c2 += [0]*es[i]

# 맨 앞 비트부터 세어보기
# 맨 뒤 비트부터 세어보기