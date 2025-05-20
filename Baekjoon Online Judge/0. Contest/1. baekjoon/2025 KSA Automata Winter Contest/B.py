import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    res = [""] * n
    total = 0
    abs_idx = 0

    for _ in range(m):
        am, pm = map(int, input().split())
        if am + pm > n:
            print('NO')
            return
        total += am + pm
        absence = min(n - am - pm, n - abs_idx)
        for i in range(abs_idx, abs_idx + absence):
            res[i] += 'X'

        idx = 0
        while am:
            if absence and idx == abs_idx:
                idx += absence
                continue
            res[idx] += '+'
            am -= 1
            idx += 1
        while pm:
            if absence and idx == abs_idx:
                idx += absence
                continue
            res[idx] += '-'
            pm -= 1
            idx += 1
        while idx < n:
            if absence and idx == abs_idx:
                idx += absence
                continue
            res[idx] += '+'
            idx += 1
        abs_idx += absence

    if total > n * (m - 1):
        print('NO')
        return
    print('YES')
    for stu in res:
        print(stu)
solution()