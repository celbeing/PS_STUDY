#14002: 가장 긴 증가하는 부분 수열 4
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [0] * N
pointer = [-1] * N
peek = 0

for i in range(N):
    for j in range(i):
        if dp[i] < dp[j] + 1 and A[i] > A[j]:
            dp[i] = dp[j] + 1
            pointer[i] = j
    if pointer[i] == -1:
        dp[i] = 1
        pointer[i] = i
    if dp[peek] < dp[i]:
        peek = i

print(dp[peek])
array = [A[peek]]
while peek != pointer[peek]:
    peek = pointer[peek]
    array.append(A[peek])
print(*reversed(array))