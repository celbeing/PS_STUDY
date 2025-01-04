# 12902: Alice and Bob
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    c = list(map(int, input().split()))
    def euc(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    k = c[0]
    for i in range(1, n):
        k = euc(k, c[i])
    print("Alice" if (max(c) // k - len(c)) & 1 else "Bob")
solution()