#C: 양갈래 짝 맞추기
import sys
input = sys.stdin.readline
N = int(input())
result = 1
while N > 1:
    result *= N-1
    N -= 2
print(result)