# 33692: 해밍 거리
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
bin_a, bin_b = [], []
c = 1
l = -1
while b >= c:
    bin_a.append(1 if a & c else 0)
    bin_b.append(1 if b & c else 0)
    c <<= 1
    l += 1
new_a, new_b = 0, 0
for i in range(l, -1, -1):
    if bin_a[i] != bin_b[i]:
        for j in range(i):
            bin_a[j] = 1
            bin_b[j] = 0
        bin_b[i] = 1
        break
c = 1
for i in range(l + 1):
    new_a += c if bin_a[i] else 0
    new_b += c if bin_b[i] else 0
    c <<= 1
print(new_a, new_b)