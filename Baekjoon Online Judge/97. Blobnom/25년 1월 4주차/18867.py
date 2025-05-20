# 18867: 편지 꼭 해다오
import sys
input = sys.stdin.readline
def solution():
    k = ord(input().rstrip())
    p = k
    for _ in range(813):
        k *= p
        k %= 20200429
    c = 1
    p = k
    while k != 20200402:
        k += p
        k %= 20200429
        c += 1
    print(c)
'''
def solution():
    t = []
    a = dict()
    mod = 20200429
    for i in range(48, 58): t.append(i)
    for i in range(65, 91): t.append(i)
    for i in range(97, 123): t.append(i)
    for i in range(62):
        k = t[i]
        a[i] = chr(k)
        for j in range(813):
            t[i] *= k
            t[i] %= mod
    def dfs(d, y, path):
        if d == 5:
            if y == 20200402:
                print(path)
            return

        for i in range(62):
            dfs(d + 1, (y + t[i]) % mod, path + a[i])
        return
    dfs(0, 0, '')
    print("there is no answer")
'''
while True:
    solution()