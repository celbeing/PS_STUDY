import random
random.random()
sieve = [1] * 100001
sieve[0] = sieve[1] = 0
testcases = [i for i in range(0, 100001)]
for i in range(2, 100001):
    if sieve[i]:
        for j in range(i * i, 100001, i):
            sieve[j] = 0
path = "C:\\Users\\kimsd\\Documents\\GitHub\\2024_BOJ\\coalla OJ\\14 소수판정-2\\"
file = open(path + "1.in", 'w+')
w = file.writelines("100000\n")
for i in range(1, 100000):
    w = file.writelines(f"{testcases[i]} ")
w = file.writelines(f"{testcases[100000]}")
file = open(path + "1.out", 'w+')
for i in range(1, 100001):
    if sieve[testcases[i]]:
        w = file.writelines('YES\n')
    else:
        w = file.writelines('NO\n')