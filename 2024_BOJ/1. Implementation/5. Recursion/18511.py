#18511: 큰 수 구성하기
import sys
input = sys.stdin.readline
miis = lambda: map(int, input().split())
def solution():
    N, K = miis()
    num = sorted(list(set(miis())))
    def dfs(n):
        ret = n
        if n > N: return 0
        for m in num:
            ret = max(ret, dfs(n * 10 + m))
        return ret
    print(dfs(0))
solution()