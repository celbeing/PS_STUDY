import sys
input = sys.stdin.readline

R,C = map(int,input().split())
A,B = map(int,input().split())
for r in range(R):
    line = ""
    for c in range(C):
        for b in range(B):
            if r + c & 1: line += "."
            else: line += "X"
    for a in range(A):
         print(line)