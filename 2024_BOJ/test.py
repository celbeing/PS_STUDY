import sys
input = sys.stdin.readline

def dsum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x //= 10
    return sum

while True:
    s = input().rstrip()
    if s == "END": break

    N = int(s)
    d = dsum(N)
    for i in range(N-1,-1,-1):
        if dsum(i) == d-1:
            print(i)
            break