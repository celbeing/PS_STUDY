from math import lcm
N = int(input())
steak = list(map(int, input().split()))
for i in range(N): steak[i] *= 2
res = 1
for s in steak: res = lcm(res, s)
print(res)