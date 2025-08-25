import random
random.random()
file = open(r"C:\Users\kimsd\OneDrive\바탕 화면\tc\1.in", 'w')
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
w = file.writelines('10000\n')
rec = dict()
lst = []
for i in range(25):
    for j in range(25):
        for k in range(16):
            t = a[i] + a[j] + a[k]
            rec[t] = random.randint(1,100)
            lst.append(t)
            w = file.writelines(f'{t} {rec[t]}\n')
random.shuffle(lst)
w = file.writelines('10000\n')
for k in lst:
    w = file.writelines(f'{k}\n')