import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    t = [0] * 200001
    count = 0
    entered = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if b:
            if t[a] == 0:
                t[a] = 1
                entered += 1
            else:
                count += 1
        else:
            if t[a]:
                t[a] = 0
                entered -= 1
            else:
                count += 1
    print(count + entered)
    return

if __name__ == '__main__':
    solution()