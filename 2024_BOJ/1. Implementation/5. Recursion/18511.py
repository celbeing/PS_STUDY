#18511: 큰 수 구성하기
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    