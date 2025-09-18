import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
rage = 0
total = 0
for b in a:
    rage += 1 if b else -1
    total += rage
print(total)