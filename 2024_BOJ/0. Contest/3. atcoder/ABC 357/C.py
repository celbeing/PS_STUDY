N = int(input())

board = [['#']*(3**N) for _ in range(3**N)]

def draw(x,y,d):
    if d == -1:
        return
    for a in range(3):
        for b in range(3):
            if a == b == 1:
                for i in range(3**d):
                    for j in range(3**d):
                        board[x+a*3**d+i][y+b*3**d+j] = '.'
            else:
                draw(x+a*3**d,y+b*3**d,d-1)

draw(0,0,N-1)
for k in board:
    print("".join(k))