import sys, random
from collections import deque
input = sys.stdin.readline
def solution():
    random.random()
    num = [i for i in range(1, int(input()) + 1)]
    random.shuffle(num)
    print(*num)
solution()