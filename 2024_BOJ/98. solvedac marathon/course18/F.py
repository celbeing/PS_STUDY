#20366: 같이 눈사람 만들래?
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    H = sorted(list(map(int, input().split())))
    gap = int(2e9)
    for i in range(N - 1):
        for j in range(i + 1, N):
            elsa = H[i] + H[j]
            a, b = 0, N - 1
            while a < b:
                if a == i or a == j: a += 1
                elif b == i or b == j: b -= 1
                else:
                    anna = H[a] + H[b]
                    if anna > elsa:
                        gap = min(gap, anna - elsa)
                        b -= 1
                    elif anna < elsa:
                        gap = min(gap, elsa - anna)
                        a += 1
                    else:
                        return 0
    return gap
print(solution())