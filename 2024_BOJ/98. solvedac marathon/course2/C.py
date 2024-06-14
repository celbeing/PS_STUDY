table = [[(1, 0), (1,-1), (1,-1), (2,-1)],
         [(0, 1), (0, 0), (0, 0), (1, 0)],
         [(0, 1), (0, 0), (0, 0), (1, 0)],
         [(-1,2), (0, 0), (0, 0), (0,-1)]]
dp = [[0]*61 for _ in range(61)]
dp[20][20] = 1

print("Round   A wins    B wins    Tie")

def prt(i,a,b,t):
    print("{:>5} {:>9.4f}%{:>9.4f}%{:>9.4f}%".format(i,a,b,t))

for i in range(1,21):
    next = [[0]*61 for _ in range(61)]
    for x in range(61):
        for y in range(61):
            for p in range(4):
                for q in range(4):
                    dx = x+table[p][q][0]
                    dy = y+table[p][q][1]
                    if 0 <= dx < 61 and 0 <= dy < 61:
                        next[dx][dy] += dp[x][y]
    dp = next[:][:]

    a,b,t = 0,0,0
    for x in range(61):
        for y in range(61):
            if x > y: a += dp[x][y]
            elif x < y: b += dp[x][y]
            else: t += dp[x][y]
    total = (a+b+t)/100
    prt(i,a/total,b/total,t/total)