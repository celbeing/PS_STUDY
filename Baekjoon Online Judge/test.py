import sys
input = sys.stdin.readline
s = list(input().strip())
n = len(s)
count = 0
for i in range(n - 2):
    if s[i + 1] == '^':
        if s[i] == s[i + 2] == '+': count += 1
        elif s[i] == s[i + 2] == '-': count -= 1

for i in range(n - 3):
    if s[i] == s[i + 3]:
        if s[i + 1] ==