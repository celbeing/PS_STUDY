#19788: Болезнь
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    vir = [1] * (n + 1)
    cln = [0] * (n + 1)
    for _ in range(m):
        data = list(map(int, input().split()))
        if data[-1]:
            for i in range(n):
                if data[i] == 0:
                    vir[i + 1] = 0
        else:
            for i in range(n):
                if data[i]:
                    cln[i + 1] = 1
    virus = []
    clean = []
    unknown = []
    for i in range(1, n + 1):
        if vir[i] and cln[i]:
            print("Incorrect")
            return
        elif vir[i]:
            virus.append(i)
        elif cln[i]:
            clean.append(i)
        else:
            unknown.append(i)
    print(len(clean), *clean)
    print(len(virus), *virus)
    print(len(unknown), *unknown)
solution()