#1972: 놀라운 문자열
import sys
input = sys.stdin.readline
def solution():
    while True:
        S = input().rstrip()
        if S == '*': break
        n = len(S)
        flag = True
        for k in range(1, n):
            t = set()
            for i in range(n - k):
                t.add(S[i] + S[i + k])
            if len(t) < n - k:
                flag = False
                break
        if flag: print(f"{S} is surprising.")
        else: print(f"{S} is NOT surprising.")
solution()