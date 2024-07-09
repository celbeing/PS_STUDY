N = int(input())
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
prime2 = []
prime3 = []
for i in range(17):
    for j in range(i+1,17):
        prime2.append(prime[i]*prime[j])
        for k in range(j+1,17):
            prime3.append(prime2[-1]*prime[k])
prime2.sort()
prime3.sort()

def fexp(n,k):
    res = 1
    while k > 0:
        if k&1:
            res *= n
        n *= n
        k >>= 1
    return res

count = 1

for p in prime:
    s,e = 2,N+1
    while s < e:
        m = (s+e)//2
        t = fexp(m,p)
        if t>N:
            e = m
        else:
            s = m+1
    while fexp(s,p) > N: s -= 1
    if s > 0: s -= 1
    if s == 0: break
    count += s

for p in prime2:
    s,e = 2,N+1
    while s < e:
        m = (s+e)//2
        t = fexp(m,p)
        if t>N:
            e = m
        else:
            s = m+1
    while fexp(s,p) > N: s -= 1
    if s > 0: s -= 1
    if s == 0: break
    count -= s

for p in prime3:
    s,e = 2,N+1
    while s < e:
        m = (s+e)//2
        t = fexp(m,p)
        if t>N:
            e = m
        else:
            s = m+1
    while fexp(s,p) > N: s -= 1
    if s > 0: s -= 1
    if s == 0: break
    count += s

print(count)