import sys
input = sys.stdin.readline
S = list(input().rstrip())
T = list(input().rstrip())
n = len(S)
X = []
while not(S == T):
    for i in range(n):
        if S[i] > T[i]:
            S[i] = T[i]
            X.append(''.join(S))
            break
    else:
        for j in range(n-1,-1,-1):
            if not(S[j] == T[j]):
                S[j] = T[j]
                X.append(''.join(S))
                break
print(len(X))
for x in X: print(x)