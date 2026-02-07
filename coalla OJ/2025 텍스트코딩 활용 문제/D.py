from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"
numb = {'영':0, '일':1, '이':2, '삼':3, '사':4, '오':5, '육':6, '칠':7, '팔':8, '구':9}
hang = '영일이삼사오육칠팔구'
for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b, c = randint(0, 9), randint(0, 9), randint(0, 9)
    while (a, b, c) in check:
        a, b, c = randint(0, 9), randint(0, 9), randint(0, 9)
        check.add((a, b, c))
    a = hang[a]
    b = hang[b]
    c = hang[c]
    w = file.writelines(f'{a} {b} {c}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{numb[a] + numb[b] + numb[c]}\n')