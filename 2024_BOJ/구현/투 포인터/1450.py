#1450: 냅색문제
import sys
input = sys.stdin.readline

N,C = map(int,input().split())
weight = list(map(int,input().split()))

'''
def putin(n, remain):
    case = 1
    for i in range(n):
        if weight[i] < remain:
            case += putin(i,remain-weight[i])
        elif weight[i] == remain:
            case += 1
    return case

result = putin(N,C)
print(result)
'''

a = N//2
b = N-a
a_sum = []
b_sum = []

for i in range(1<<a):
    a_sum.append(0)
    for j in range(a):
        if i&(1<<j):
            a_sum[-1]+=weight[j]

for i in range(1<<b):
    b_sum.append(0)
    for j in range(b):
        if i&(1<<j):
            b_sum[-1]+=weight[j+a]
b_sum.sort()
result = 0

def binarysearch(k):
    s = 0
    e = len(b_sum)
    while s < e:
        m = (s+e)//2
        if b_sum[m] > k:
            e = m
        else:
            s = m+1
    return e

for A in a_sum:
    if C-A >= 0:
        result += binarysearch(C-A)

print(result)