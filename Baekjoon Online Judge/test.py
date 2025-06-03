w, p = map(int, input().split())
l = list(map(int, input().split()))
check = [0] * (w + 1)
check[-1] = 1
for i in range(p):
    check[l[i]] = 1
    check[w - l[i]] = 1
    for j in range(i + 1, p):
        check[l[j] - l[i]] = 1
res = []
for i in range(1, w + 1):
    if check[i]: res.append(i)
print(*res)