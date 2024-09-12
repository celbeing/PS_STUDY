#4504: 배수 찾기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    while True:
        k = int(input())
        if k:
            if k % n:
                print(f"{k} is NOT a multiple of {n}.")
            else:
                print(f"{k} is a multiple of {n}.")
        else:
            return
solution()