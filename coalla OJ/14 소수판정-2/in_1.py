import random
random.random()
prime = []
sieve = [1] * 100001
sieve[0] = sieve[1] = 0
for i in range(2, 100001):
    if sieve[i]:
        prime.append(i)
        for j in range(i * i, 100001, i):
            sieve[j] = 0
random.shuffle(prime)
testcases = [0, 100000, 99991]
for _ in range(25):
    testcases.append(prime.pop())
    testcases.append(random.randint(1,100000))
path = "C:\\Users\\kimsd\\OneDrive\\바탕 화면\\tc\\"
for i in range(1, 53):
    file = open(path + f"{i}.in", 'w+')
    w = file.writelines(f"{testcases[i]}")
    file = open(path + f"{i}.out", 'w+')
    if sieve[testcases[i]]:
        w = file.writelines('YES')
    else:
        w = file.writelines('NO')
