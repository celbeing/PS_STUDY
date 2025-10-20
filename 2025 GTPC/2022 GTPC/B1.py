a, b, c, d = map(int, input().split())
count = 0
while a or b or c or d:
    a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
    count += 1
print(count)