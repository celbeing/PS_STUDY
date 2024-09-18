#9079: 동전 게임
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        coins = [list(input().rstrip()) for _ in range(3)]
