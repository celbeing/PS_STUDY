import random, math
random.random()
inf = 1 << 31

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"
for i in range(1, 21):
    a = random.randint(1, 100000000)
    b = random.randint(1, 100000000)
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    w = file.writelines(f"{a} {b}")


    file = open(path + f"{i}.out", "w+", encoding='utf-8')
    w = file.writelines(f'{(a + b) << 1}')