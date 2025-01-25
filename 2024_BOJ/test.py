import sys
from collections import deque
input = sys.stdin.readline
def solution():
    print(sys.getsizeof(deque([])))
solution()