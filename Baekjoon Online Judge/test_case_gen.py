import random, math
random.random()
inf = 1 << 31
mod = int(1e9) + 7

def euc(a, b):
    while b:
        a, b = b, a % b
    return a

sieve = [0] * 10001
sieve[0] = 1
sieve[1] = 1
prime = []
for i in range(2, 10001):
    if sieve[i]: continue
    prime.append(i)
    for j in range(i * i, 10001, i):
        sieve[j] = 1

print('done')

path = r"C:\Users\kimsd\Desktop\tc\\"

for tc in range(1, 21):
    n = random.randint(1, 10000)
    file = open(path + f"{tc}.in", "w+", encoding = 'utf-8')
    w = file.writelines(f'{n}')

    dp = [0] * (n + 1)
    dp[0] = 1
    for p in prime:
        if p > n: break
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
            dp[i] %= mod


    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{dp[-1]}')