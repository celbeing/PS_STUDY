# 7558: 제곱잉여
import sys
input = sys.stdin.readline
def solution(i):
    a, p = map(int, input().split())
    a %= p
    
    print(f"Scenario #{i}:")
    print()