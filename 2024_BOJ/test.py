N = int(input())
P = int(input())
res = P
if N >= 5: res = min(res, P - 500)
if N >= 10: res = min(res, (P // 10) * 9)
if N >= 15: res = min(res, P - 2000)
if N >= 20: res = min(res, (P // 4) * 3)
print(max(res, 0))