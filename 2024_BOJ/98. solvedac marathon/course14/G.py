#16158: 회식구호
import sys
input = sys.stdin.readline
def satisfy(P, D):
    return ((P - abs(P - D)) / P) * 100

def solution():
    N, X, K = map(int, input().split())
    loud = list(map(int, input().split()))
    