#B: 하늘과 핑크
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(sum(B),sum(A))