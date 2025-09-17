# 9246: 다트판
import sys
from math import exp
input = sys.stdin.readline

a, b, c, d, e, f = map(float, input().split())
sigma = (float(input()) ** 2) * 2
a = (50 * (1 - exp(-a ** 2 / sigma))
     + 25 * (exp(-a ** 2 / sigma) - exp(-b ** 2 / sigma))
     + 10.5 * (exp(-b ** 2 / sigma) - exp(-c ** 2 / sigma))
     + 31.5 * (exp(-c ** 2 / sigma) - exp(-d ** 2 / sigma))
     + 10.5 * (exp(-d ** 2 / sigma) - exp(-e ** 2 / sigma))
     + 21 * (exp(-e ** 2 / sigma) - exp(-f ** 2 / sigma)))
print(a)