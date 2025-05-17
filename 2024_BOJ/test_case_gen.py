import random, math
random.random()

path = r"C:\Users\kimsd\Desktop\tc\\"

for i in range(1, 5):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    m = int(input())
    p = int(input())
    w = file.writelines(f"{m}\n{p}")
    m += round(m * p / 100, 0)
    m += round(m * p / 100, 0)
    m += round(m * p / 100, 0)
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{int(m)}")