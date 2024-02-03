#A번 - A + B - C
A = int(input())
B = int(input())
C = int(input())
print(A+B-C)
b = 1
while B // b > 0:
    b *= 10
print(A*b+B-C)