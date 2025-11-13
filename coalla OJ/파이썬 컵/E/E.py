import random

path = r"C:\Users\kimsd\Documents\GitHub\PS_STUDY\Coalla OJ\파이썬 컵\E\\"
check = {2001, 2501}
for tc in range(3, 31):
    y = random.randint(2001, 1000000)
    while y in check:
        y = random.randint(2001, 1000000)
    check.add(y)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{y - 1}\n')
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    if y % 4 == 0:
        if y % 400 == 0:
            w = file.writelines(f'{y}.02.29.\n')
        elif y % 100 == 0:
            w = file.writelines(f'{y}.02.28.\n')
        else:
            w = file.writelines(f'{y}.02.29.\n')
    else:
        w = file.writelines(f'{y}.02.28.\n')
