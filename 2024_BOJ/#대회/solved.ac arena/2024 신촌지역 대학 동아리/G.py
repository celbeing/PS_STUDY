# G: AND, OR, XOR 2
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.append(2**31)
div = 998_244_353
bit = [0 for _ in range(31)]

AND = 0
for a in A:
    for i in range(31):
        if a < 1<<i: break
        if a & 1<<i:
            bit[i] += 1
        else:
            AND += (bit[i]*(bit[i]+1)//2)*(1<<i)
            AND %= div
            bit[i] = 0

print(AND)