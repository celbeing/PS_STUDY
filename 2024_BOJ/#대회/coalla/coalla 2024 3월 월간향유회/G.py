#17609: 회문
import sys
input = sys.stdin.readline
T = int(input())

def palin(t):
    s, e = 0, len(t)-1

    semi = False
    while s < e:
        if t[s] != t[e]:
            semi = True
            break
        s += 1
        e -= 1
    else:
        return 0

    ss1,se1 = s+1,e
    ss2,se2 = s,e-1
    while ss1 < se1:
        if t[ss1] != t[se1]:
            break
        ss1 += 1
        se1 -= 1
    else:
        return 1
    while ss2 < se2:
        if t[ss2] != t[se2]:
            return 2
        ss2 += 1
        se2 -= 1
    else:
        return 1

for _ in range(T):
    print(palin(input().rstrip()))