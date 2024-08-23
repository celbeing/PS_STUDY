S = int(input())
A = int(input())
B = int(input())
res = 250
while A < S:
    A += B
    res += 100
print(res)