#14469: 소가 길을 건너간 이유 3
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    cow = [tuple(map(int, input().split())) for _ in range(N)]
    cow.sort()
    time = 0
    for arr, chk in cow:
        if arr > time: time = arr + chk
        else: time += chk
    print(time)
solution()