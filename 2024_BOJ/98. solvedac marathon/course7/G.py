import sys
input = sys.stdin.readline

def bin(k):
    s,e = 0,len(S)
    while s < e:
        m = (s+e)//2
        if S[m] < k: s = m+1
        elif S[m] > k: e = m
        else: return m
    return -1

N = int(input())
U = sorted([int(input()) for _ in range(N)])
S = []
for i in range(N):
    for j in range(i,N):
        if U[i]+U[j] >= U[-1]: break
        S.append(U[i] + U[j])
S.sort()

for k in range(N-1,2,-1):
    for x in range(k):
        yz = bin(U[k]-U[x])
        if yz >= 0:
            print(U[k])
            exit()