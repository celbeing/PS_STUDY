#9252: LCS 2
import sys
input = sys.stdin.readline
A = list(input().rstrip())
B = list(input().rstrip())
DP = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
for i in range(len(B)):
    for j in range(len(A)):
        if B[i] == A[j]:
            DP[i+1][j+1] = DP[i][j] + 1
        else:
            DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])

print(DP[len(B)][len(A)])
lcs = []
i,j = len(B),len(A)
while i > 0 and j > 0:
    if DP[i][j] == DP[i][j-1]:
        j-=1
    elif DP[i][j] == DP[i-1][j]:
        i-=1
    else:
        lcs.append(B[i-1])
        i-=1
        j-=1
print(''.join(reversed(lcs)))