#4797: 화학
import sys
input = sys.stdin.readline

def getatom(k):
    name = chem[k]
    count = 0
    k += 1
    if k < N and chem[k].islower():
        name += chem[k]
        k += 1
        if k < N and chem[k].islower():
            name += chem[k]
            k += 1
    while k < N and chem[k].isdigit():
        count *= 10
        count += int(chem[k])
        k += 1
    if count == 0: count = 1
    return (name,count,k)

def bracket(k):
    stack = dict()
    while k < N and not chem[k] == ')':
        if chem[k] == '(':
            inside,k = bracket(k+1)
            for atom in inside:
                if atom in stack:
                    stack[atom] += inside[atom]
                else:
                    stack[atom] = inside[atom]
        else:
            name,count,k = getatom(k)
            if name in stack:
                stack[name] += count
            else:
                stack[name] = count
    k += 1
    mult = 0
    while k < N and chem[k].isdigit():
        mult *= 10
        mult += int(chem[k])
        k += 1
    if mult == 0: mult = 1
    for atom in stack:
        stack[atom] *= mult
    return (stack,k)

while True:
    chem = input().rstrip()
    if chem == "": break
    N = len(chem)
    atoms, k = bracket(0)
    atomcount = []
    for atom in atoms:
        atomcount.append((atom,atoms[atom]))
    atomcount.sort()
    result = ""
    for i in range(len(atomcount)-1):
        if atomcount[i][1] > 1:
            result += str(atomcount[i][1])
        result += atomcount[i][0]+'+'
    if atomcount[-1][1] > 1:
        result += str(atomcount[-1][1])
    result += atomcount[-1][0]
    print(result)