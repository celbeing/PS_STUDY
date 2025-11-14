import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\L\\"
for tc in range(1, 31):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines()

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines()