#3863: 행복한 전화 통화
import sys
input = sys.stdin.readline
def solution():
    while True:
        N, M = map(int, input().split())
        if N == M == 0: break
        a = []
        for i in range(1, N + 1):
            src, dst, st, du = map(int,input().split())
            a.append((st, st + du, i))
        for i in range(M):
            result = set()
            st, du = map(int, input().split())
            du += st
            for s, e, i in a:
                if not(e <= st or s >= du):
                    result.add(i)
            print(len(result))
solution()