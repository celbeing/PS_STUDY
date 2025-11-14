a, b = map(int, input().split())
lcd = a
while lcd % b > 0:
    lcd += a
print(lcd)