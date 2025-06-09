# 30805: 사전 순 최대 공통 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def solution(a, b, res = []):
    if not(a and b):
        return res

    max_a, max_b = max(a), max(b)
    idx_a, idx_b = a.index(max_a), b.index(max_b)

    if max_a == max_b:
        res.append(max_a)
        return solution(a[idx_a + 1:], b[idx_b + 1:], res)
    elif max_a > max_b:
        a.pop(idx_a)
        return solution(a, b, res)
    else:
        b.pop(idx_b)
        return solution(a, b, res)

result = solution(a, b)
print(len(result))
if result: print(*result)