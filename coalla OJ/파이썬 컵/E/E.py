import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\E\\"
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
            w = file.writelines(f'366\n')
        elif y % 100 == 0:
            w = file.writelines(f'365\n')
        else:
            w = file.writelines(f'366\n')
    else:
        w = file.writelines(f'365\n')
