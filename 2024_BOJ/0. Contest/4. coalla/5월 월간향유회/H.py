T = list(input())
S = ""
A = []
n = 0
while n <= len(T)//2:
    now = T[n]
    a = 0
    for i in range(n,len(T), n+1):
        if now == T[i]: a += 1
        else: break
    S += now
    A.append(a)
    n = n*(a+1)+a
print(S)
print(*A)