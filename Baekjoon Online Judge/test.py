import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = list(input().strip())
    n = int(len(s) ** 0.5)
    res = ''
    for i in range(n - 1, -1, -1):
        for j in range(i, len(s), n):
            res += s[j]
    print(res)