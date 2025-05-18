import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for i in range(1, 10):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    rps = input().strip()
    ym = input().strip()
    w = file.writelines(f"{rps}\n{ym}")
    sel = input().strip()
    res = input().strip()
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{sel}\n{res}")