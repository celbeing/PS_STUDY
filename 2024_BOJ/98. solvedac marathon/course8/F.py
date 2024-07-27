N,M = map(int,input().split())
useless = []
C = 1
for i in range(1,N-1):
    C *= N-i
    C //= i
    if C % M: continue
    else: useless.append(i+1)
print(len(useless))
for k in useless:
    print(k)