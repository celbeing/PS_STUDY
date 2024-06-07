#17626: Four Squares
n = int(input())
inf = 50000
DP = [inf] * 50001
DP[0] = 0
for i in range(1, n+1):
    k = 1
    while k**2 <= i:
        if DP[i-k**2]+1<DP[i]:
            DP[i] = DP[i-k**2]+1
        k += 1
print(DP[n])