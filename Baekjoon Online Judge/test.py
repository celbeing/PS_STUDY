recaman = set()
n = 0
num = 1
while n < 1000:
    if n - num <= 0 or n - num in recaman:
        n += num
    else:
        n -= num
    recaman.add(n)
    print(f'{num}: {n}')
    num += 1