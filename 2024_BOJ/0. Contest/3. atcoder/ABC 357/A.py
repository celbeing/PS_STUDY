import sys

input = sys.stdin.readline
N,M = map(int,input().split())
H = list(map(int,input().split()))
count = 0
for k in H:
    if M >= k:
        M -= k
        count += 1
    else: break
print(count)