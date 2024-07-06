import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
card = dict()
for a in A:
    if a in card:
        card[a] += 1
    else:
        card[a] = 1
result = 1
for a in card.values():
    result *= a+1
print((result-1)%int(1e9+7))