import sys
from collections import deque
from bisect import bisect_right as bi
from bisect import bisect_left as bi_l
input = sys.stdin.readline
def solution():
    l = [1,2,3,3,3,3,4,5,6,6,7]
    print(bi(l, 3))
    print(bi_l(l, 3))
solution()