# 16921: 로마 숫자 만들기 2

def solution():
    def comb(k):
        res = (k - 1) * (k - 2) * (k - 3) // 6
        res += 2 * (k ** 2) + 2
        return res

    n = int(input())
    small = [0, 4, 10, 20, 35, 56, 83, 116, 155, 198, 244, 292, 341, 390, 439]
    if n < 15: print(small[n])
    else:
        res = comb(n)
        res -= comb(n - 6) + comb(n - 8) - comb(n - 14)
        res += n - 7
        print(res)
solution()

def solution2():
    n = int(input())
    small = [1, 4, 10, 20, 35, 56, 83, 116, 155, 198, 244, 292]
    if n < 12: print(small[n])
    else: print(n * 49 - 247)

def calc(n):
    rome = [1, 5, 10, 50]
    checked = [0]
    count = dict()
    def dfs(c, i, v, x, l, d, t):
        if d == n:
            if c in count:
                count[c].append((i,v,x,l))
                checked[0] += 1
            else:
                count[c] = [(i,v,x,l)]
            return
        for k in range(t, 4):
            if k == 0:
                dfs(c + 1, i + 1, v, x, l, d + 1, 0)
            elif k == 1:
                dfs(c + 5, i, v + 1, x, l, d + 1, 1)
            elif k == 2:
                dfs(c + 10, i, v, x + 1, l, d + 1, 2)
            else:
                dfs(c + 50, i, v, x, l + 1, d + 1, 3)
    dfs(0, 0, 0, 0, 0, 0, 0)
    res = len(count)
    return res, res + checked[0], checked[0]