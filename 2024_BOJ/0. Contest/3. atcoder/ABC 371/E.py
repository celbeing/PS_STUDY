import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    idx = [0] * 200001
    dis = 0
    for i in range(N):
        count[i] = (i**2 + i * 3 + 2) // 2
        if idx[A[i]]:
            dis += idx[A[i]]
        idx[A[i]] = i + 1
        count[i] -= dis
    print(sum(count))
solution()