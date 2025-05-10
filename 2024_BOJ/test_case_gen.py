import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    a = random.randint(0,50000)
    w = file.writelines(f"{a}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{50000-a}")