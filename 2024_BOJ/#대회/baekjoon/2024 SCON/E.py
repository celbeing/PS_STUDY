import sys
input = sys.stdin.readline
N = int(input())
A = list(input().split())
C = True
if input().rstrip() == "F": C = False
pre = True
if A[0] == "T": pre = True
else: pre = False

if N == 1:
    if pre == C: print(0)
    else: print(1)
    exit()

for i in range(2, N-2,2):
    next = True
    if A[i] == "T": next = True
    else: next = False
    if A[i-1] == "&": pre = pre and next
    else: pre = pre or next

last = True
if A[-1] == "T": last = True
else: last = False

if C:
    if A[-2] == "&":
        if pre and last:
            print(0)
        elif pre or last:
            print(1)
        else:
            print(2)
    else:
        if pre or last:
            print(0)
        else:
            print(1)
else:
    if A[-2] == "&":
        if pre and last:
            print(1)
        else:
            print(0)
    else:
        if pre and last:
            print(2)
        elif pre or last:
            print(1)
        else:
            print(0)