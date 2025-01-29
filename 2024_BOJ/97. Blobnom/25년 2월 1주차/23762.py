# 23762: 배드민턴 복식 팀 만들기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    m = sorted(enumerate(list(map(int, input().split()))), key = lambda x: x[1])
    
    res = 0
    if n % 4:
        for i in range(0, n, 4):
            res += m[i + 3] - m[i]
        print(res)
    else:
