import sys
input = sys.stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
a = [(p[i], i) for i in range(1, n + 1)]
a.sort()

k = n - 1
low, high, sum, total = 0, a[-1][0], 0, 0
peek = 0
res = n - 1

while k >= 0:
    low = a[k][0]
    sum += a[k][0]
    total = low + high + sum
    if peek < total:
        peek = total
        res = k
    k -= 1

print(n - res)
module = []
for i in range(res, n):
    module.append(a[i][1])
print(*module)