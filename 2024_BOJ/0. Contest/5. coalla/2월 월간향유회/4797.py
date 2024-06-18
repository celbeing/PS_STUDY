#4797: 화학
import sys
input = sys.stdin.readline()

def getatom(i):
    name = chem[i]
    num = 1
    for k in range(1,4):
        if i+k == n: break
        if chem[i+k].isalpha() and chem[i+k].islower():
            name += chem[i+k]
        else:
            if chem[i+k].isdigit():
                num = int(chem[i+k])
            break
    return (name,num)

def bracket(f):
    now = f+1
    ret = dict
    while not chem[now] == ")":
        while not chem[now].isupper(): now += 1
        name,num = getatom(now)
        if name in ret: ret[name] += num
        else: ret[name] = num
    if now+1 < n and chem[now+1].isdigit()
    for atom in ret:

for chem in input:
    n = len(chem)
    i = 0
    atoms = dict()
    while i < n: