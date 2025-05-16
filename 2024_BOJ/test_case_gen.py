import random, math
random.random()

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for i in range(1, 51):
    file = open(path + f"{i}.in", "w+", encoding = 'utf-8')
    ask = input().strip()
    ans = input().strip()
    w = file.writelines(f"{ask}\n{ans}")
    file = open(path + f"{i}.out", "w+", encoding = 'utf-8')
    if ask == ans:
        w = file.writelines("신원 확인 되었습니다.")
    else:
        w = file.writelines("누구냐!")