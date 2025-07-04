import random
p = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
dp = [0] * 101
dp[0] = 1
for i in range(1, 26):
    for j in range(p[i], 101):
        dp[j] += dp[j - p[i]]

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"
check = set()
for tc in range(21, 22):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    k = 100
    w = file.writelines(f'{k}')
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{dp[k]}')