#23561: Young한 에너지는 부족하다
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    age = sorted(list(map(int, input().split())))
    print(age[N * 2 - 1] - age[N])
solution()