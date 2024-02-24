#28064: 이민희진
import sys
input = sys.stdin.readline
N = int(input())
namelist = []

def link(a,b):
    flag = False
    na = len(a)
    nb = len(b)
    for i in range(1,min(na,nb)+1):
        if a[-i:] == b[:i] or a[:i] == b[-i:]:
            flag = True
            break
    return flag

count = 0
for i in range(N):
    name = list(input().rstrip())
    for k in namelist:
        if link(k,name):
            count += 1
    namelist.append(name)

print(count)