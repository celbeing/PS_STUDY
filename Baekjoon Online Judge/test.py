n = int(input())
old, young = 0, 0
old_name, young_name = '', ''
name, d, m, y = input().split()
old_name = young_name = name
old = young = int(y) * 10000 + int(m) * 100 + int(d)
for _ in range(n - 1):
    name, d, m, y = input().split()
    k = int(y) * 10000 + int(m) * 100 + int(d)
    if k < old:
        old = k
        old_name = name
    if k > young:
        young = k
        young_name = name
print(young_name)
print(old_name)