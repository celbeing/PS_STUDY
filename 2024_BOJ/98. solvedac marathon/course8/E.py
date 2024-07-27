import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
score = sorted([tuple(map(int,input().split())) for _ in range(N)], key = lambda x:x[1])
org = 0
for i in range(K):
    org += score.pop()[0]
score.sort()
for i in range(M):
    org += score.pop()[0]
print(org)