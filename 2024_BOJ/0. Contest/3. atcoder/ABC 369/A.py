import sys
input = sys.stdin.readline
A,B = map(int,input().split())
if A==B: print(1)
elif max(A,B)-min(A,B) & 1: print(2)
else: print(3)