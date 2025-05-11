import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    S = input().strip()
    w = file.writelines(f"{S}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines("{0:*^40}".format(S))