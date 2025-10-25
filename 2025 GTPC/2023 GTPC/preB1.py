import sys
input = sys.stdin.readline

led = list(map(int, input().split()))
fp, np = 1, 0

n_led = led[:]
n_led[0] ^= 1
n_led[1] ^= 1

for i in range(1, len(led) - 1):
    if n_led[i - 1]:
        fp += 1
        n_led[i] ^= 1
        n_led[i + 1] ^= 1
    if led[i - 1]:
        np += 1
        led[i] ^= 1
        led[i + 1] ^= 1
if n_led[-2] and n_led[-1]: fp += 1
elif n_led[-2] or n_led[-1]: fp = -1

if led[-2] and led[-1]: np += 1
elif led[-2] or led[-1]: np = -1

if fp < 0: print(np)
elif np < 0: print(fp)
else: print(min(fp, np))