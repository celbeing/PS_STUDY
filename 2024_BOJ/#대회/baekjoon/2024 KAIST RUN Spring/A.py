import sys
input = sys.stdin.readline
T = int(input())
run = [0,1,11,111,1_111,11_111,111_111,1_111_111,11_111_111,111_111_111,1_111_111_111,11_111_111_111,111_111_111_111,1_111_111_111_111,11_111_111_111_111,111_111_111_111_111,1_111_111_111_111_111,11_111_111_111_111_111]
for _ in range(T):
    N,K = map(int,input().split())
    RUN = []
    d = 10**(N-1)
    while K > 9:
        dr = 17
        while run[dr] > K: dr-=1
        time = 1
        while run[dr]*time <= K and time < 10: time += 1
        time -= 1
        RUN.append(run[dr]*time)
        K-=RUN[-1]
    if K > 0: RUN.append(K)
    print(len(RUN))
    print(*RUN)