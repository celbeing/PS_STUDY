#10347: Reverse Rot
import sys
input = sys.stdin.readline
def solution():
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
    while True:
        crypt = list(input().split())
        if crypt[0] == '0': break
        encrypt = list(crypt[1])
        encrypt.reverse()
        move = int(crypt[0])
        for i in range(len(encrypt)):
            encrypt[i] = alpha[(alpha.index(encrypt[i]) + move) % 28]
        print(''.join(encrypt))
solution()