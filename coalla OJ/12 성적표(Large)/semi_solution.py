import sys
input = sys.stdin.readline
def solution():
    table = []
    for _ in range(int(input())):
        table.append(tuple(map(str, input().split())))
    for _ in range(int(input())):
        c = input().strip()
        for name, score in table:
            if name == c:
                print(score)
                break
solution()