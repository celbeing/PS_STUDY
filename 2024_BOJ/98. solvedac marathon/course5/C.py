import sys
input = sys.stdin.readline
T = int(input())

def luck(n):
    while n > 0:
        m = n%10
        if not(m == 5 or m == 8):
            return False
        n //= 10
    return True

for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    M = int(input())
    B = list(map(int,input().split()))
    K = int(input())
    C = list(map(int,input().split()))

    result = set()
    for i in range(N):
        for j in range(M):
            for k in range(K):
                t = A[i]+B[j]+C[k]
                if luck(t): result.add(t)
    print(len(result))