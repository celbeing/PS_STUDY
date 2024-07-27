r = 1001
for _ in range(int(input())):
    A,B = map(int,input().split())
    if B < A: continue
    if B < r: r = B
print(-1 if r == 1001 else r)