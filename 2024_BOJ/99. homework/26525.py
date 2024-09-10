#26525: 빙고
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 공부할 것: 기댓값의 선형성