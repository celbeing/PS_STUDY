import sys
input = sys.stdin.readline
def solution():
    def euc(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    total = 20358520
    case = [6612900,9730740,2532816,732160,282060,39780,39780,205976,165984,14664,1472,188]
    print(sum(case))
    for c in case:
        t = euc(total, c)
        print(f"{c//t}/{total//t}")
solution()