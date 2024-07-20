import sys
input = sys.stdin.readline
for _ in range(int(input())):
    sent = list(input().split())
    print(*(sent[2:]+sent[:2]))