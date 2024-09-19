import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    for i in range(2, N + 1):
        A[i] += A[i - 1]
    for _ in range(int(input())):
        i, j = map(int, input().split())
        print(A[j] - A[i - 1])
solution()