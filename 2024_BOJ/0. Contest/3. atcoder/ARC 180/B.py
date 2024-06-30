import sys
input = sys.stdin.readline
N,K = map(int,input().split())
P = list(map(int,input().split()))
record = []

def find():
    m = N
    l,r = N,N
    for i in range(N-K):
        for j in range(i+K,N):
            if m > P[j]-P[i]:
                l,r = i,j
                m = P[j]-P[i]
    return l,r

