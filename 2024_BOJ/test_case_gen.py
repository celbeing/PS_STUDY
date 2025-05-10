import random, math
random.random()

path = r"C:\Users\kimsd\Desktop\tc"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    a = int(input())
    w = file.writelines(f"{a}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    if a & 1:
        w = file.writelines(f"한 명 남아요.")
    else:
        w = file.writelines(f"출발!")