import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
count = 1
k = 0
streak = 2
while k < N-1:
    if S[k] != S[k+1]:
        streak += 1
    else:
        count *= streak//2
        streak = 2
        count %= 1000000007
    k += 1
count *= streak//2
count %= 1000000007
print(count)