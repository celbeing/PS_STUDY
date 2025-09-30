# X1 모둠 만들기1
# TEST CASE GENERATOR
from random import randint, shuffle
from heapq import heappush, heappop
from collections import deque

path = r"C:\Users\kimsd\OneDrive\Documents\카카오톡 받은 파일\2025GTPCforms\(25.09.22)02 (양식)GTPC문제및데이터(출제자이름)\X1\\"

for tc in range(6, 11):
    A = randint(2, 10)
    B = randint(A, 10)
    N = randint(A, 100)
    S = [randint(-25, 25) for i in range(N)]
    shuffle(S)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{N} {A} {B}\n')
    line = f'{S[0]}'
    for i in range(1, N):
        line += f' {S[i]}'
    w = file.writelines(f'{line}\n')

    INF = int(1e9)

    S.append(-INF)
    S.sort()
    dp = [INF] * (N + 1); dp[0] = 0

    for i in range(A, N + 1):
        for j in range(i - A + 1, max(i - B, 0), -1):
            diff = S[i] - S[j]
            dp[i] = min(dp[i], dp[j - 1] + diff)

    file = open(path + f'{tc}.ans', 'w+', encoding='utf-8')
    w = file.writelines(f'{dp[N] if dp[N] < INF else -1}')