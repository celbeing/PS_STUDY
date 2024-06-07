# D: PPC 만들기
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
S = list(input().rstrip())
c,p=0,N-1
for i in range(K):
    while c < N and S[c] == 'P': c+=1
    while p >= 0 and S[p] == 'C': p-=1
    if p < c: break
    S[c] = 'P'
    S[p] = 'C'
result = 0
pcount = 0
for k in S:
    if k == 'P': pcount += 1
    elif pcount < 2: continue
    else:
        result += pcount*(pcount-1)//2
print(result)