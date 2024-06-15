import sys
from itertools import combinations
input = sys.stdin.readline
N,M = map(int,input().split())
S = [[] for _ in range(N)]
for i in range(N):
    s = list(input().rstrip())
    for j in range(M):
        if s[j] == 'o':
            S[i].append(1)
        else:
            S[i].append(0)
fc = [i for i in range(N)]
for i in range(1,N+1):
    p = combinations(fc,i)
    for k in p:
        popcorn = [0] * M
        for j in k:
            for l in range(M):
                if S[j][l]: popcorn[l] = 1

        if popcorn == [1]*M:
            print(i)
            exit()