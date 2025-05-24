import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"
for i in range(1, 21):
    n = random.randint(1, 10)
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    w = file.writelines(f"{n}")
    m = 1
    l = []
    for _ in range(n):
        k = random.randint(1, 1000)
        if k < 10:
            k = 0
        else:
            k = random.randint(1, 10)
        w = file.writelines(f"\n{k}")
        l.append(k)
    file = open(path + f"{i}.out", "w+", encoding='utf-8')
    for i in range(n - 1):
        m *= l[i]
        if m:
            w = file.writelines(f"{m}\n")
        else:
            w = file.writelines(f"0이잖아")
            break
    else:
        m *= l[-1]
        if m:
            w = file.writelines(f"{m}")
        else:
            w = file.writelines("0이잖아")