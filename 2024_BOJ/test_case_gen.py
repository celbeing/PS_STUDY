import random, math
random.random()

path = r"C:\Users\kimsd\Desktop\tc\\"

for i in range(1, 21):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    n = random.randint(1,999)
    w = file.writelines(f"{n}")
    count = 0
    a, b, c = n // 100, (n % 100) // 10, n % 10
    tri = (3, 6, 9)
    if a in tri: count += 1
    if b in tri: count += 1
    if c in tri: count += 1
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{n if count == 0 else '짝!' * count}")