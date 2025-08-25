file = open(r"C:\Users\kimsd\OneDrive\바탕 화면\tc\1.in", 'r')
n = int(file.readline())
d = dict()
for _ in range(n):
    name, score = map(str, file.readline().split())
    d[name] = int(score)
m = int(file.readline())
res = []
for _ in range(m):
    name = file.readline().strip()
    res.append(d[name])
file = open(r"C:\Users\kimsd\OneDrive\바탕 화면\tc\1.out", 'w+')
for r in res:
    w = file.writelines(f'{r}\n')