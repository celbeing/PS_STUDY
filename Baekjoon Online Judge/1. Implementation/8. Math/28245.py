import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    r = []
    for i in range(63):
        if m & 1<<i:
            r.append(i)
    if m == 1:
        print(0,0)
    elif len(r) == 1:
        print(r[0]-1,r[0]-1)
    elif len(r) == 2:
        print(*r)
    elif len(r) > 2:
        a = 1<<r[-1]
        a += 1<<r[-2]
        b = 1<<r[-1]
        b += 1<<r[-2]+1
        if m-a > b-m:
            print(r[-2]+1,r[-1])
        else:
            print(r[-2],r[-1])