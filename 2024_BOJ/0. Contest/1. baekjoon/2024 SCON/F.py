import sys
input = sys.stdin.readline
N = int(input())
A = []
B = []
if N%3 == 0:
    for i in range(1, N+1, 3):
        A.append(i)
        A.append(i+1)
        B.append(i+2)
elif N%3 == 2:
    A.append(1)
    B.append(2)
    for i in range(3, N, 3):
        A.append(i)
        A.append(i+1)
        B.append(i+2)
else:
    for i in range(2, N+1, 3):
        A.append(i)
        A.append(i+1)
        B.append(i+2)
print(len(A))
print(*A)
print(len(B))
print(*B)