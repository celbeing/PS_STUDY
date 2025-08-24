<<<<<<< Updated upstream
=======
prime = []
sieve = [1] * 1000001
sieve[0] = sieve[1] = 0
for i in range(2, 1001):
    if sieve[i]:
        prime.append(i)
        for j in range(i * i, 1000001, i):
            sieve[j] = 0
for i in range(1000, 1000001):
    if sieve[i]: prime.append(i)

a, b = map(int, input().split())
res = b - a + 1
lim = b ** 0.5
check = [1] * res
for i in prime:
    if i > lim: break
    sq = i * i
    for j in range((((a - 1) // sq) + 1) * sq, b + 1, sq):
        if check[j - a]:
            check[j - a] = 0
            res -= 1
print(res)
>>>>>>> Stashed changes
