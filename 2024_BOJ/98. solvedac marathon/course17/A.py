#5691: 평균 중앙값 문제
import sys
input = sys.stdin.readline
def solution():
    while True:
        A, B = map(int, input().split())
        if A == B == 0: break
        if min(A, B) * 3 - A - B <= min(A, B):
            print(min(A, B) * 3 - A - B)
        elif not((A + B) & 1):
            print((A + B) // 2)
        elif max(A, B) * 3 - A - B >= max(A, B):
            print(max(A, B) * 3 - A - B)
solution()