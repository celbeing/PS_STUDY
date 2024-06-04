#G: Move or Block!
import sys
input = sys.stdin.readline
N = int(input())
board = list(input().rstrip())
l,r,c = 0,0,0
stone = False
for i in range(N):
    if board[i] == '.':
        l += 1
        c += 1
    elif board[i] == 'X':
        l = 0
    else:
        c -= l
        break
for i in range(N-1,-1,-1):
    if board[i] == '.':
        r += 1
        c += 1
    elif board[i] == 'X':
        r = 0
    else:
        c -= r
        break

if l == 0 or r == 0:
    print("mingyu")
    exit()

if l == 1:
    if (r + c) % 2 == 0:
        print("mingyu")
    elif r == 1:
        print("yunsu")
    else:
        print("draw")
    exit()

if r == 1:
    if (l + c) % 2 == 0:
        print("mingyu")
    elif l == 1:
        print("yunsu")
    else:
        print("draw")
    exit()

print("draw")