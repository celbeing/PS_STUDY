#6574: 새로운 과일
import sys
input = sys.stdin.readline
def solution():
    while True:
        fruits = input()
        if fruits == "": return
        a, b = fruits.split()
        n, m = len(a), len(b)

        lcs = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        result = ""
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if lcs[i][j] == lcs[i - 1][j]:
                result = a[i] + result
                i -= 1
            elif lcs[i][j] == lcs[i][j - 1]:
                result = b[j] + result
                j -= 1
            else:
                result = a[i] + result
                i -= 1; j -= 1
        while i >= 0:
            result = a[i] + result
            i -= 1
        while j >= 0:
            result = b[j] + result
            j -= 1
        print(result)
solution()