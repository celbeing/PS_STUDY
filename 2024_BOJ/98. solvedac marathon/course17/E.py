#24552: 올바른 괄호
import sys
input = sys.stdin.readline
def solution():
    S = list(input().rstrip())
    right = [0] * len(S)
    left = [0] * len(S)
    for i in range(len(S)):
        right[i] = right[i - 1] + 1 if S[i] == "(" else right[i - 1] - 1
        left[i] = left[i - 1] + 1 if S[-(i + 1)] == ")" else left[i - 1] - 1
    res = 0
    if right[-1] == 1:
        for i in range(len(S) - 1, -1, -1):
            if right[i] == 0: break
            elif S[i] == "(": res += 1
    else:
        for i in range(len(S) - 1, -1, -1):
            if left[i] == 0: break
            elif S[-(i + 1)] == ")": res += 1
    print(res)
solution()