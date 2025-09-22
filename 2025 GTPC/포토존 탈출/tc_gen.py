import random
from heapq import heappush, heappop
from collections import deque

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

dp = [0] * 38
dp[0] = 1
dp[1] = 2
dp[2] = 3
for i in range(3, 38):
    dp[i] = dp[i - 2] + dp[i - 3] + 1
shell = [0] * 38
shell[2] = 1
for i in range(3, 38):
    shell[i] = shell[i - 1] + dp[i - 3] ** 2

nums = [i for i in range(1, 38)]
random.shuffle(nums)
for tc in range(1, 38):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = nums.pop()
    w = file.writelines(f'{n}\n')

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    if n == 1: res = 1
    else: res = (dp[n] - 1) * (dp[n - 1]) - shell[n]
    w = file.writelines(f'{res}\n')