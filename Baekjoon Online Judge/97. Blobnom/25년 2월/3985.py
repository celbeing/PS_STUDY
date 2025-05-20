# 3985: 롤 케이크
import sys
input = sys.stdin.readline
def solution():
    l = int(input())
    n = int(input())
    cake = [1] * (l + 1)
    expect = 0
    maxget = 0
    e_num = 0
    m_num = 0
    for i in range(1, n + 1):
        p, k = map(int, input().split())
        if k - p  > expect:
            expect = k - p
            e_num = i
        count = 0
        for j in range(p, k + 1):
            if cake[j]:
                cake[j] = 0
                count += 1
        if count > maxget:
            maxget = count
            m_num = i
    print(e_num)
    print(m_num)
solution()