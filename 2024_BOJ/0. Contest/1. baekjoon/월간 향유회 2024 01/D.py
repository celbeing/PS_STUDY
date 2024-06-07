#D번 - LR
import sys
input = sys.stdin.readline
alpha = "abcdefghijklmnopqrstuvwxyz"
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    letter = list(input().rstrip())
