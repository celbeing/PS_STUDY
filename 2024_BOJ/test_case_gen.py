import random, math
random.random()

path = r"C:\Users\kimsd\Desktop\tc\\"

for i in range(7, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    p, c, h = map(int, input().split())
    w = file.writelines(f"{p}\n{c}\n{h}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    w = file.writelines("피자"*p)
    w = file.writelines("\n")
    w = file.writelines("치킨"*c)
    w = file.writelines("\n")
    w = file.writelines("햄버거"*h)