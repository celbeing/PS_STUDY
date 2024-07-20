import sys
N,K = map(int,input().split())
S = sorted(list(input().rstrip()))
now = S[0]
alpha = [1]
for i in range(1,N):
    if S[i] == now:
        alpha[-1] += 1
    else:
        now = S[i]
        alpha.append(1)
print(alpha)