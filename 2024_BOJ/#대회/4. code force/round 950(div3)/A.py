import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(input().rstrip())
    count = [0]*7
    for k in a:
        count[ord(k)-ord('A')] += 1
    result = 0
    for c in count:
        if c < m: result += m-c
    print(result)