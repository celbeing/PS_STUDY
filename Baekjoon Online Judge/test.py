n = int(input())
a = 1
k = 0
while a < n:
    a <<= 1
    k += 1
b = 1
while not(n & b):
    b <<= 1
    k -= 1
print(a, k)
