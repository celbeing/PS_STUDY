import sys
input = sys.stdin.readline
def solution():
    letter = input().rstrip()
    mod = 20200429
    y = 0
    for l in letter:
        k = ord(l)
        for i in range(813):
            k *= ord(l)
            k %= mod
        y += k
    y %= mod
    print(y)
solution()