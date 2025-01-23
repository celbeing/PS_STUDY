# 28286: 재채점을 기다리는 중
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    answer = list(map(int, input().split()))
    marked = list(map(int, input().split()))

    def check(ans, mark):
        count = 0
        for i in range(n):
            if ans[i] == mark[i]: count += 1
        return count

    def remark(ans, d, res):
        if d == k:
            score = check(ans, answer)
            if score > res:
                return score
            else:
                return res

        ret = 0
        for i in range(n):
            ans_nxt = [0] * n
            for j in range(i):
                ans_nxt[j] = ans[j]
            for j in range(i + 1, n):
                ans_nxt[j] = ans[j - 1]
            p = remark(ans_nxt, d + 1, res)
            if ret < p: ret = p
        for i in range(n):
            ans_nxt = [0] * n
            for j in range(i):
                ans_nxt[j] = ans[j]
            for j in range(i, n - 1):
                ans_nxt[j] = ans[j + 1]
            p = remark(ans_nxt, d + 1, res)
            if ret < p: ret = p
        p = remark(ans, d + 1, res)
        if ret < p: ret = p
        return ret

    print(remark(marked, 0, 0))
solution()