a, b, k = map(int, input().split())
res = [0] * (k + 1)
for i in range(k + 1):
    res[i] = a // b
    a = (a % b) * 10
if a // b >= 5: res[-1] += 1
for i in range(k, 0, -1):
    if res[i] < 10: break
    res[i] %= 10
    res[i - 1] += 1
num = str(res[0])+"."
for i in range(1, k + 1):
    num += str(res[i])
print(num)