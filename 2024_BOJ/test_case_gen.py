import random, math
random.random()

path = "C:\\Users\\kimsd\\OneDrive\\바탕 화면\\"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    a = input().strip()
    w = file.writelines(f"{a}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f"{len(a.replace(' ', ''))}")