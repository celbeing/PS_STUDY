import sys
input = sys.stdin.readline
def solution():
    rec = list(input().strip())
    a, b = 0, 0
    for i in range(0, len(rec), 2):
        if rec[i] == 'A':
            a += int(rec[i + 1])
        else:
            b += int(rec[i + 1])
    print('A' if a > b else 'B')
solution()