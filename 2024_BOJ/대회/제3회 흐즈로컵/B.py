#B: 슈퍼 소수
import sys
input = sys.stdin.readline
eratos = [True for _ in range(318138)]
eratos[0] = False
eratos[1] = False
prime = [0]
for i in range(318138):
    if eratos[i]:
        prime.append(i)
        j = i*2
        while j < 318138:
            eratos[j] = False
            j += i

T = int(input())
for t in range(T):
    print(prime[prime[int(input())]])