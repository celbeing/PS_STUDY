import random, math
random.random()

path = r"C:\Users\kimsd\Desktop\tc\\"

for i in range(6, 21):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    a = random.randint(2,999)
    w = file.writelines(f"{a}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{a ** 2}\n{a ** 3}")