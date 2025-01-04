import math

MAXN = 10009

x = [0] * MAXN
vals = set()
N, X = 0, 0

def solve(p):
    global X, N, vals, x

    n = X // p
    if n <= 2 or n > N:
        return False
    vals.clear()

    i, pnxt = 0, p
    while i < N and x[i] < pnxt:
        vals.add(x[i] + p)
        i += 1
    pnxt += p
    found = False

    while i < N:
        found = False
        while i < N and x[i] < pnxt:
            if x[i] in vals:
                vals.add(x[i] + p)
                found = True
            i += 1
        if not found:
            return False
        pnxt += p
    return pnxt > X

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    results = []

    global N, X, x

    while idx < len(data):
        N = int(data[idx])
        if N == 0:
            break
        idx += 1
        ans = -1

        x[0] = 0
        for i in range(1, N + 1):
            x[i] = int(data[idx])
            x[i] += x[i - 1]
            idx += 1
        X = x[N]

        for i in range(1, int(math.sqrt(X)) + 1):
            if X % i == 0:
                if solve(i):
                    ans = max(ans, X // i)
                if solve(X // i):
                    ans = max(ans, i)

        if ans == -1:
            results.append(str(ans))
        else:
            results.append(str(N - ans))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
