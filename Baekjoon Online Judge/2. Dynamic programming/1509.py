#1509: 팰린드롬 분할
import sys
input = sys.stdin.readline

array = list(input().rstrip())
n = len(array)
array.insert(0,'0')
palin = [[] for _ in range(n + 1)]
for i in range(1,n+1):
    j = 0
    while i-j > 0 and i+j <= n:
        if array[i-j] == array[i+j]:
            palin[i+j].append(i-j)
            j += 1
        else: break
    j = 0
    while i-j > 0 and i+j+1 <= n:
        if array[i-j] == array[i+j+1]:
            palin[i+j+1].append(i-j)
            j += 1
        else: break
DP = [2500] * (n + 1)
DP[0] = 0
for i in range(1,n+1):
    for k in palin[i]:
        if k == 0:
            DP[i] = 1
            break
        if DP[i] > DP[k-1]+1:
            DP[i] = DP[k-1]+1
print(DP[n])