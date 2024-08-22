from math import gcd

x = int(input())
y = int(input())
k = gcd(x,y)
print(x//k, y//k)