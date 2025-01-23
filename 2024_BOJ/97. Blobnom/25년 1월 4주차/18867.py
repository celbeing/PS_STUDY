# 18867: 편지 꼭 해다오
import sys
input = sys.stdin.readline
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
                exit()
            return

        for i in range(62):
            dfs(d + 1, (y + t[i]) % mod, path + a[i])
        return
    dfs(0, 0, '')
    print("there is no answer")
solution()