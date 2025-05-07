import random, math
random.random()

path = "C:\\Users\\kimsd\\OneDrive\\바탕 화면\\"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w")
    a, b = map(str, input().split())
    w = file.writelines(f"{a} {b}")
    file = open(path + f"{i}.out", "w")
    w = file.writelines(f"{a}와{b}")