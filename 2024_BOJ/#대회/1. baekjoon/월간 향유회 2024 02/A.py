#A: 준영이
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
if N > M:
    tmp = N
    N = M
    M = tmp
Nr = N%3
Mr = M%3
result = 1
triple = 0
couple = 0

if Nr*Mr == 0:
    triple = N*M//3
elif Nr*Mr == 1:
    triple = (N//3)*M
    triple += M//3
    if triple > 0:
        triple -= 1
        couple += 2
elif Nr*Mr == 2:
    if Nr == 1:
        triple = (N//3)*M
        triple += M//3
        couple = 1
    else:
        triple = (M//3)*N
        triple += N//3
        couple = 1
else:
    triple = (M//3)*N+(N//3)*2
    couple = 2

for _ in range(triple):
    result *= 3
    result %= 1_000_000_007
for _ in range(couple):
    result *= 2
    result %= 1_000_000_007

print(result)