import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    s = S[l-1:r]
    high = 0
    for i in range(len(s)):
        sum = 0
        for j in range(i + 1):
            if i+j+1 == len(s): break
            if s[i-j] == s[i+j+1]: sum += 1
        if high < sum: high = sum
    print(high)