#31003: 언젠가 정렬이 될 수 있으면 좋겠네
import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int,input().split())]

def euc(a,b):
    while b > 0:
        a,b = b,a%b
    if a == 1: return True
    return False

