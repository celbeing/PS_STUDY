import sys
input = sys.stdin.readline
def solution():
    result = dict()
    for _ in range(int(input())):
        a, b = map(str, input().split())
        result[a] = int(b)
    for _ in range(int(input())):
        print(result[input().strip()])
solution()