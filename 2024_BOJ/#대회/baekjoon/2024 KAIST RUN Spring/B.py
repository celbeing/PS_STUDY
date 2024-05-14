import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int,input().split()))
result = (n**2+n)//2
for i in range(1,n):
    ab = 0
    ba = 0
    for j in range(n-i):
        if s[j] > s[j+i]:
            ba += 1
            result += (ab**2+ab)//2
            ab = 0
        elif s[j+i] > s[j]:
            ab += 1
            result += (ba**2+ba)//2
            ba = 0
        else:
            ab += 1
            ba += 1
    result += (ab**2+ab+ba**2+ba)//2
print(result)