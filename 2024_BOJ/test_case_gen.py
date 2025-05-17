import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for i in range(1, 21):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    a = int(input())
    w = file.writelines(f"{a}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    if a >= 7:
        w = file.writelines(f"걷자")
    elif a >= 4:
        w = file.writelines(f"뛰자")
    else:
        w = file.writelines(f"다음 거 타자")