# 11565: 바이너리 게임
import sys
input = sys.stdin.readline
def solution():
    a = list(input().strip())
    b = list(input().strip())
    A, B = 0, 0
    for aa in a:
        if aa == '1': A += 1
    for bb in b:
        if bb == '1': B += 1
    if A & 1: A += 1
    if A < B: print("DEFEAT")
    else: print("VICTORY")
solution()