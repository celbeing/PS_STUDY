# 4808: Max Q(최대 동압) 시점 찾기(Large)
import sys
from math import floor, ceil
input = sys.stdin.readline

def dens(a, t, x):
    return (t - x) * (a * x)**2

def solution():
    a, t = map(int, input().split())
    p = floor(t * 2 / 3)
    q = ceil(t * 2 / 3)
    print(p if dens(a, t, p) >= dens(a, t, q) else q)

solution()