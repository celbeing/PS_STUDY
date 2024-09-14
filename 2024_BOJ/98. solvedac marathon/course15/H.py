#23820: MEX
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = sorted(list(set(map(int, input().split()))))
    checked = set()
    if 0 in a:
        for k in a:
            for t in a:
                if k*t > 2000003: break
                checked.add(k*t)
        k = 1
        while True:
            if not k in checked: return k
            k += 1
    else: return 0
print(solution())