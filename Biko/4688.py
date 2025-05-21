# 4688: 무한 길이 물풍선
x, y, r = set(), set(), set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a in x: r.add(a)
    if b in y: r.add(-b)
    x.add(a)
    y.add(b)
print(len(r))