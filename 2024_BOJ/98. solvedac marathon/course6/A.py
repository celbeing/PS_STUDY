board = list(input())
N = len(board)
result = ""
count = 0
for i in range(N):
    if board[i] == 'X':
        count += 1
    else:
        if count & 1:
            print(-1)
            exit()
        for k in range(count//4):
            result += "AAAA"
        if (count//2)&1: result += "BB"
        result += "."
        count = 0
if count > 0:
    if count & 1:
        print(-1)
        exit()
    for k in range(count//4):
        result += "AAAA"
    if (count//2)&1: result += "BB"
print(result)