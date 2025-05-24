import random, math
random.random()
inf = 1 << 31

path = r"C:\Users\kimsd\Desktop\tc\\"
for i in range(1, 21):
    n = random.randint(1, 100000000)
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    w = file.writelines(f"{n}")


    file = open(path + f"{i}.out", "w+", encoding='utf-8')
    while n > 1:
        if n % 2: n = n * 3 + 1
        else: n >>= 1
        if n == 1: break
        if n >= inf: print('overflow')
        w = file.writelines(f'{n}\n')
    w = file.writelines(f'{n}')