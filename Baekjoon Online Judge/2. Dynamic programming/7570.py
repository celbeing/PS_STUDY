# 7570: 줄 세우기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
st = [0] * (n + 1)
high = 0
for k in a:
    st[k] = st[k - 1] + 1
print(n - max(st))