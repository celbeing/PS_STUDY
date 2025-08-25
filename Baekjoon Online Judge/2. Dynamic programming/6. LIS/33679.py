# 33679: 세기의 대결
import sys
input = sys.stdin.readline

def find(arr, k):
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if arr[m] < k:
            s = m + 1
        else:
            e = m
    return e

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    yj, hg = 0, 0
    for i in range(-n, 0, 1):
        stack = [a[i]]
        for j in range(i + 1, i + n, 1):
            if stack[-1] < a[j]:
                stack.append(a[j])
            else:
                p = find(stack, a[j])
                stack[p] = a[j]
        yj = max(yj, len(stack))

    for i in range(-n, 0, 1):
        stack = [b[i]]
        for j in range(i + 1, i + n, 1):
            if stack[-1] < b[j]:
                stack.append(b[j])
            else:
                p = find(stack, b[j])
                stack[p] = b[j]
        hg = max(hg, len(stack))

    if yj < hg: print("HG Win!")
    elif yj > hg: print("YJ Win!")
    else: print("Both Win!")
solution()