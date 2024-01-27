#9252: LCS 2
import sys
input = sys.stdin.readline
A = list(input().rstrip())
B = list(input().rstrip())
DP = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
trace = [0]*(len(B)+1)
for i in range(len(B)):
    for j in range(len(A)):
        if B[i] == A[j]:
            DP[i+1][j+1] = DP[i][j] + 1
            trace[i+1] = i
        else:
            DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])
            trace[i+1] = trace[i]
print(DP[len(B)][len(A)])
result = [trace[len(B)]]
while result[-1] > -1:
    result.append(trace[result[-1]-1])
print(*result)