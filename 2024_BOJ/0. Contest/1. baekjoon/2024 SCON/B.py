import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    team = input().rstrip()
    S = list(team)
    num = 0
    upp = 0
    low = 0
    for c in S:
        if str(c).isupper():
            upp += 1
        elif str(c).islower():
            low += 1
        elif str(c).isdigit():
            num += 1
    if upp > low: continue
    if len(S) > 10: continue
    if len(S) == num: continue
    print(team)
    break